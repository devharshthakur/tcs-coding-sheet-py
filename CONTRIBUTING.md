# Contributing

Thank you for contributing to this project. Please follow below given guidelines

## Before you start to contribute

1. First discuss with me about your contribution (if contribution is huge like solving entirely a new problem) before starting so that we both are on the same page.

2. If the contribution you about to make is small such as simple corrections , adding coments etc, please do it without any discussion and directly create a pr

3. This project follows a simple straight forward pr based workflow

## PR workflow

1. Create a fork of the project in your account
2. Create a branch, branch name should follow [conventional commit guidelines](https://www.conventionalcommits.org/en/v1.0.0/). Below are few examples
3. When changes are made review them
4. When chages are reviewed run the follwing commands:-
   - `uv run ruff check`
   - `uv format`
   - `git add .` which add all tracked and untracked files as well
5. Then create a commit, commit should follow [conventional commit guidelines](https://www.conventionalcommits.org/en/v1.0.0/).
6. Create a pull request with your changes.

### Note

1. For [Step 4](#pr-workflow), I have created a bash script called [commit](./scripts//commit.bash) which does the same things in the given order. To use it, I have already created a just target for it.

#### What it does:

1. runs `uv format && uv run ruff check`
2. stages all changes with `git add .`
3. opens a temporary commit message file in `vim`, add the details and then `:wq` (write and quit) the file
4. asks for confirmation before running `git commit`

I have also created a just target to run the script. To run the script run `just c`

2. For [Step 6](#pr-workflow), I have also provided a [template](./.github/pull_request_template.md), if you want you can use that too.
   > Note: remove placeholders in the commit file (which is opened in vim) so those do not get included in the commit message.
