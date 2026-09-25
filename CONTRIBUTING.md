# Contributing

## Workflow

1. Pull the latest `main`: `git pull origin main`
2. Create a branch: `git checkout -b <username>/<short-topic>` (e.g. `ravzaatasdemir/grover`)
3. Add your work, commit with a clear message, push, and open a pull request.
4. At least one other member skims the PR before merging. Keep PRs small — one topic per PR.

## Where things go

| What | Where | Naming |
|------|-------|--------|
| A notebook on a study topic | `notebooks/<topic>/` | `<username>_<short-name>.ipynb` (e.g. `ravzaatasdemir_grover_3qubit.ipynb`) |
| A short note or summary | `notes/` | `<topic>.md`; add your section under your name if the file exists |
| Code others can import | `src/qsim/` | Add a docstring and a small usage example |
| Unfinished or personal experiments | `members/<username>/` | Anything goes |
| A new resource | `RESOURCES.md` | One row: name, what it is good for, link |

## Rules

- **Never commit API tokens.** Keep your IBM Quantum token in environment variables or a local file listed in `.gitignore`.
- **Do not upload copyrighted books or paid material.** Link to them instead.
- **Keep notebooks light.** Clear large outputs before committing (Kernel → Restart & Clear Output, then re-run only what is needed for plots).
- **Use the shared environment.** If you need a new package, add it to `requirements.txt` in the same PR.
- **Explain, don't just paste.** Each notebook starts with a short Markdown cell: what it does, which resource it follows, and what you learned.
