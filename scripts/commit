#!/usr/bin/env bash

set -euo pipefail

uv format
git add .

# Write the commit message in a temporary file so Vim can edit it safely.
tmpfile=$(mktemp "${TMPDIR:-/tmp}/commit-message.XXXXXX")
cleanup() {
  rm -f "$tmpfile"
}
trap cleanup EXIT

# Seed the buffer with a simple template for title and description.
cat >"$tmpfile" <<'EOF'
Title

Description
EOF

# Open the message in Vim instead of inline terminal prompts.
vim "$tmpfile"

# Parse the edited file: first line is the title, anything after the blank line is the body.
title=""
description=""
line_no=0
while IFS= read -r line || [[ -n "$line" ]]; do
  case "$line_no" in
    0)
      title="$line"
      ;;
    1)
      ;;
    *)
      if [[ -z "$description" ]]; then
        description="$line"
      else
        description+=$'\n'$line
      fi
      ;;
  esac
  line_no=$((line_no + 1))
done <"$tmpfile"

# A commit without a title is not useful, so stop early.
if [[ -z "$title" ]]; then
  printf 'Aborted: commit title is empty.\n'
  exit 1
fi

printf '\nCommit preview:\n'
printf 'Title: %s\n' "$title"
printf 'Description: %s\n' "$description"
read -r -p "Commit these changes? [y/N] " confirm

case "$confirm" in
  y|Y|yes|YES)
    git commit -m "$title" -m "$description"
    ;;
  *)
    printf 'Aborted.\n'
    exit 1
    ;;
esac
