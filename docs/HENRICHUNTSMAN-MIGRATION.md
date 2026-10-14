# HenricHuntsman profile migration checklist

Checked 2026-10-14 using connected GitHub repository inventory.

## Confirmed
- Account owner now appears as `HenricHuntsman`.
- 31 repositories are visible in the connected account inventory (26 public, 5 private).
- The old profile README repository is still `HenricHuntsman/SpidermanTotro`.
- No repository named `HenricHuntsman/HenricHuntsman` was found.
- The profile README refresh exists on branch `docs/profile-refresh-20261014` (PR #4 from before the account rename).
- Existing original README on `main` still contains old `SpidermanTotro` links.

## Must-do manual steps (do not automate without approval)
1. Review the open profile README pull request and merge only after verifying the links and content.
2. In `https://github.com/HenricHuntsman/SpidermanTotro/settings`, rename the repository **SpidermanTotro** to **HenricHuntsman**. This is what activates GitHub's special profile README.
3. Confirm `https://github.com/HenricHuntsman` displays the README from the new `HenricHuntsman/HenricHuntsman` repository.
4. Check GitHub Pages and any domains, OAuth callbacks, Actions badges, release links, packages and integrations.
5. Search local repositories for `SpidermanTotro` and update hard-coded URLs and remotes as needed.
6. Keep five private repositories private; do not publish internal paths or secrets.
7. Replace the placeholder SVG with a properly licensed, credited huntsman photograph only after sourcing it.

## Safe local inspection

```bash
gh auth status
gh repo list HenricHuntsman --limit 100 --json name,visibility,url --jq '.[] | [.name,.visibility,.url] | @tsv'
git remote -v
git grep -n -I 'SpidermanTotro' || true
```

Do not delete or force-push any repository as part of this migration.
