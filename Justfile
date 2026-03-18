lint:
    uv run ty check
alias l := lint

format:
    uv format --preview-features format
alias fmt := format

precommit: lint format
alias pc := precommit

commit:
    @scripts/commit
alias c := commit
