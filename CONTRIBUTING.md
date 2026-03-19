# Contributing

Thank you for contributing to this project. Please follow below given guidelines

## Before you start to contribute

1.  **Large Contributions:** If you plan to solve an entirely new problem or make significant architectural changes, please open an issue first and reach out to me. It is important that we are on the same page before you invest your time.

2.  **Small Fixes:** For minor corrections like fixing typos, improving documentation, or adding comments, feel free to create a issue with a Pull Request attached directly without prior discussion.

> Note: Before opening a new issue, please check if a similar one already exists.

3.  Creating an issue first is mandatory for new work. Please follow the [Issue Guidelines](#issue-guidelines) before starting any implementation.

4.  If the issue is already assigned to you, you can begin the workflow below. For big or unclear issues, ask first before doing anything else so we can confirm the approach. Refer 1 and 2 above

5.  This project follows a simple straight forward pr based workflow.

## PR workflow

1. **Create or reference an issue first** and make sure it is assigned before starting work.
2. **Fork the project** to your own GitHub account if needed.
3. **Create a branch** for your changes only after the issue is assigned and approved for work. Branch names should follow [conventional commit guidelines](https://www.conventionalcommits.org/en/v1.0.0/#specification).
   - _Examples:_ `feat/add-login-system`, `fix/broken-header`, `docs/update-readme`
4. **Review your changes** once you have finished coding.
5. **Prepare your changes** by running the following quality checks:
   - `uv run ruff check` (lint all the files)
   - `uv format` (format all the files)
   - `git add .` (This stages all changes, including new files)
6. **Commit your changes** commit should follow [conventional commit guidelines](https://www.conventionalcommits.org/en/v1.0.0/#specification).
7. **Create a Pull Request** with a clear description of your changes and link the related issue.

## Issue Guidelines

1.  **Title:** Use [conventional commit style](https://www.conventionalcommits.org/) for the title.
    - _Example:_ `fix: broken search pagination` or `feat: add dark mode support`
2.  **Description:** Keep it concise but descriptive. Explain what the problem is and how it behaves.
3.  **Proposed Fix:** If you have an idea of how to solve it, please include a brief "Proposed Fix" section.

### Issue Labels and Workflow

Please use the labels below while contributing. This is compulsory.

| Label                    | When to use it                                                                               |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| `discussion`             | For issues that are being used for discussion only.                                          |
| `documentation`          | For improvements or additions to documentation.                                              |
| `duplicate`              | For issues or pull requests that already exist.                                              |
| `good first issue`       | For small tasks that are good for newcomers.                                                 |
| `bug`                    | For broken behavior or something that is not working as expected.                            |
| `feature`                | For new features or requests.                                                                |
| `fix`                    | For general fixes that are not limited to bugs, such as docs or feature-related corrections. |
| `high priority`          | For issues that should be handled first.                                                     |
| `medium priority`        | For issues that should be handled next.                                                      |
| `low priority`           | For issues that can be handled later.                                                        |
| `issue:accepted`         | For external issues that have been reviewed and accepted to move forward.                    |
| `issue:under review`     | For external issues that have been opened and are waiting for maintainer review.             |
| `issue:working`          | For accepted issues that someone has started working on.                                     |
| `issue:ready for review` | For completed work that is waiting for maintainer review on the PR.                          |

If an issue is opened without the right label or workflow state, it may be rejected until it is updated properly.

## Helpful Tools

### Automated Commit Script

To simplify **Step 4** and **Step 5**, I have created a bash script located at `./scripts/commit.bash`. You can run this easily using the provided `just` target:

```bash
just c
```

**What this script does:**

1.  Runs `uv format && uv run ruff check`.
2.  Stages all changes with `git add .`.
3.  Opens a temporary commit file in `vim`. Add your details, then save and quit (`:wq`).
4.  Asks for confirmation before running `git commit`.

> **Note:** Please remove any placeholder text in the vim buffer so it doesn't end up in your final commit message.

### PR Template

I have provided a [Pull Request template](./.github/pull_request_template.md). Please use it when opening your PR to help me understand your contribution better.
