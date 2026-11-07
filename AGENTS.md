# Androskills repository work

The main checkout and GitHub `main` should agree after a publishing task finishes.

- Before publishing, fetch the remote and inspect the current branch, staged and
  unstaged changes, untracked skill folders, and local/remote history. A skill
  existing on disk does not mean its files are committed or published.
- Preserve existing edits. If histories diverge, retain a recovery point and
  reconcile them; avoid publishing from an old remote base that omits local work.
- Temporary worktrees are useful for isolation. After publishing from one,
  reconcile its published commits into the primary checkout before declaring
  synchronization complete. Do not silently leave a second divergent `main`.
- Confirm the intended skill files are tracked in the main checkout and present
  on the remote branch. Confirm ahead/behind counts after the push.
- Preserve unrelated private material and do not force-push or discard edits to
  make histories appear synchronized. Remove temporary worktrees only when clean
  and no longer needed; keep recovery branches when useful.
