lint:
    uv run ty check
alias l := lint

format:
    uv run mdformat README.md CONTRIBUTING.md CODE_OF_CONDUCT.md CHECKLIST.md .github/pull_request_template.md
    uv run yamlfix .github/ISSUE_TEMPLATE/*.yml
    uv format --preview-features format
alias fmt := format

precommit: lint format
alias pc := precommit

commit:
    @scripts/commit
alias c := commit
