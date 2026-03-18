# Contributing

Thank you for contributing to this Python rewrite of the original TCS NQT coding sheet.

## Contribution Guidelines

1. Discuss the task with the maintainer before starting any work.
2. Confirm the scope and expected outcome before making changes.
3. Keep changes small, focused, and consistent with the existing style.
4. Update `CHECKLIST.md` or related documentation when a problem is completed.
5. Keep the code clean, readable, and well organized.

## Clean Pull Request Workflow

Please follow the below pr based workflow for the contribution:

1. Align on the task and scope.
2. Make the changes in a focused branch or working set.
3. Update the checklist or documentation as needed.
4. Review the diff carefully.
5. Use `./scripts/commit` to format, stage, and create the commit.
6. Open a pull request with a clear title and description.
7. Address review feedback if any changes are requested.

## Commit workflow

I use `scripts/commit` to format, stage, and create commits. A just command is also provided ot fire the script

```bash
just c
```

What it does:

- runs `uv format && uv run ruff check`
- stages all changes with `git add .`
- opens a temporary commit message file in `vim`, add the details and then `:wq` (write and quit) the file
- asks for confirmation before running `git commit`

### Commit message format

- First line: short title
- Blank line
- Then: a simple description

> Note : remove placeholders in the commit file(which is opened in vim) so those does not get included in the commit message

## Before submitting changes

- [ ] Format the code
- [ ] Update `CHECKLIST.md` if needed
- [ ] Review the diff
- [ ] Use `./scripts/commit` to create the commit (optional)
