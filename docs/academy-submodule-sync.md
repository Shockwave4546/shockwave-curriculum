# Syncing shockwave-curriculum into shockwave-programming-academy

`shockwave-programming-academy` (the Nuxt app that actually serves lessons/examples/
exercises/narrated-lessons to students, at `localhost:3000/sections/...`) pulls this
repo's content in as a git submodule at `content/shockwave-curriculum`. Its
`content.config.ts` reads `lessons/`, `examples/`, `exercises/` as `@nuxt/content`
collections; `public/narrated-lessons` is a symlink into the same submodule checkout.

**The gotcha:** the submodule is its own independent working tree, checked out at
whatever commit its pointer says — it does **not** see uncommitted changes made in this
repo's own working directory, even though both are clones of the same GitHub repo. Editing
`shockwave-curriculum/lessons/foo.md` has zero effect on the running academy dev server
until the submodule is updated.

## Correct procedure (do this, in order)

1. Make and verify changes in `shockwave-curriculum` as normal.
2. Commit and push them here first:
   ```bash
   git add -A
   git commit -m "..."
   git push
   ```
3. In `shockwave-programming-academy`, update the submodule to the new commit:
   ```bash
   cd content/shockwave-curriculum
   git checkout main   # or: git fetch && git checkout <new-sha>
   git pull
   cd ../..
   git add content/shockwave-curriculum
   git commit -m "Bump shockwave-curriculum submodule to <short-sha>"
   git push
   ```
   `git submodule update --remote content/shockwave-curriculum` does steps 3's `cd`+`pull`
   in one shot if the submodule is already tracking the right branch.
4. If the academy dev server (`npm run dev`) is already running, no restart is needed for
   content changes — `@nuxt/content` picks up file changes in `content/` via its own
   watcher. A restart *is* needed if `content.config.ts` itself changed.

## Local-only preview shortcut (never a substitute for the above)

While iterating on a fix, it's much faster to copy the in-progress files straight into the
submodule's working tree and check them against the *already-running* dev server, without
waiting on a commit/push/bump cycle each time:

```bash
cp -r shockwave-curriculum/narrated-lessons/. \
      shockwave-programming-academy/content/shockwave-curriculum/narrated-lessons/
```

This lands **uncommitted** changes directly in the submodule checkout — perfect for
verifying a fix live before doing the real commit+push+bump, but it must never be the last
step: the submodule checkout will still show `nothing to commit` at that new commit
afterward, and the next `git submodule update` (by anyone, including CI) wipes it. Always
follow up with the real procedure above once the fix is confirmed.

## Why not just point the submodule at a branch and auto-pull?

Nothing wrong with that as a future improvement — right now the submodule tracks a fixed
commit (detached HEAD), which is the git-submodule default and keeps academy's content
frozen to a deliberately-chosen curriculum snapshot rather than silently moving under it.
