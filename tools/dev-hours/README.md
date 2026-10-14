# Private development-hours tracker

This is an **opt-in, local-only** Python standard-library utility. It measures time between explicit `start` and `stop` commands, not keyboard activity, and never connects to GitHub or any other service.

## Usage (Ubuntu / Python 3)

```bash
python3 tools/dev-hours/dev_hours.py start --project rabbit-code
python3 tools/dev-hours/dev_hours.py status
python3 tools/dev-hours/dev_hours.py stop
python3 tools/dev-hours/dev_hours.py report --month 2026-10
```

Raw logs are saved to `~/.local/share/henric-dev-hours/sessions.csv` and active session state to `active.json`. Directory permissions are set to 0700 and files to 0600 on compatible systems. Override the location with `HENRIC_DEV_HOURS_DIR`.

**Privacy:** Logs stay on the local machine. Do not commit CSV files or private project labels. A public README hours badge should be added only after you review and approve aggregated figures. The timer does not automatically pause for inactivity or recover elapsed time after crashes; stop sessions when you stop working.

**Progress bars:** Use completed checklist items divided by an agreed milestone count. Do not use commits as a proxy for development hours.
