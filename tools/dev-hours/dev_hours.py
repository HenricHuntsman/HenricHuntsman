#!/usr/bin/env python3
"""Private, standard-library-only development time logger.

Data is stored locally. No network calls or automatic GitHub publishing.
Usage:
  python3 dev_hours.py start --project rabbit-code
  python3 dev_hours.py stop
  python3 dev_hours.py status
  python3 dev_hours.py report --month 2026-10
"""
import argparse
import csv
import datetime as dt
import json
import os
from pathlib import Path

BASE = Path(os.environ.get("HENRIC_DEV_HOURS_DIR", str(Path.home() / ".local" / "share" / "henric-dev-hours")))
STATE = BASE / "active.json"
LOG = BASE / "sessions.csv"
FIELDS = ["project", "started_at", "ended_at", "minutes"]

def now():
    return dt.datetime.now(dt.timezone.utc)

def setup():
    BASE.mkdir(parents=True, exist_ok=True)
    try:
        BASE.chmod(0o700)
    except OSError:
        pass

def read_state():
    return json.loads(STATE.read_text()) if STATE.exists() else None

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    start = sub.add_parser("start")
    start.add_argument("--project", required=True, help="Public-safe label; do not include secrets or private paths")
    sub.add_parser("stop")
    sub.add_parser("status")
    report = sub.add_parser("report")
    report.add_argument("--month", help="YYYY-MM, in UTC")
    args = parser.parse_args()
    setup()
    active = read_state()
    if args.command == "start":
        if active:
            parser.error("A session is already running; stop it first.")
        if not args.project.strip() or len(args.project) > 64:
            parser.error("Project label must contain 1-64 characters.")
        STATE.write_text(json.dumps({"project": args.project.strip(), "started_at": now().isoformat()}))
        STATE.chmod(0o600)
        print("Started local session:", args.project)
    elif args.command == "stop":
        if not active:
            parser.error("No active session.")
        end = now()
        started = dt.datetime.fromisoformat(active["started_at"])
        mins = round(max(0, (end - started).total_seconds() / 60), 2)
        new_file = not LOG.exists()
        with LOG.open("a", newline="") as fp:
            writer = csv.DictWriter(fp, fieldnames=FIELDS)
            if new_file:
                writer.writeheader()
            writer.writerow({"project": active["project"], "started_at": started.isoformat(), "ended_at": end.isoformat(), "minutes": mins})
        LOG.chmod(0o600)
        STATE.unlink()
        print(f"Saved {mins:.2f} minutes locally for {active['project']}.")
    elif args.command == "status":
        print(json.dumps(active, indent=2) if active else "No active session.")
    elif args.command == "report":
        month = args.month or now().strftime("%Y-%m")
        try:
            dt.datetime.strptime(month, "%Y-%m")
        except ValueError:
            parser.error("Month must be YYYY-MM.")
        totals = {}
        if LOG.exists():
            with LOG.open(newline="") as fp:
                for row in csv.DictReader(fp):
                    if row["ended_at"][:7] == month:
                        totals[row["project"]] = totals.get(row["project"], 0.0) + float(row["minutes"])
        print(f"Local development time for {month} (UTC end date):")
        for project, minutes in sorted(totals.items()):
            print(f"  {project}: {minutes/60:.2f} hours")
        print(f"TOTAL: {sum(totals.values())/60:.2f} hours")
        print("Nothing was uploaded.")
if __name__ == "__main__":
    main()
