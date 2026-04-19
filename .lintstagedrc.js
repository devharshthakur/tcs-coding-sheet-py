/** @type {import('lint-staged').Config} */
export default {
  "*.{ts,tsx,js,jsx}": ["prettier --write"],
  "*.py": ["uv format --preview-features format", "uv run ty check"],
  "{*.md,*.json,*.yml,*.yaml}": ["prettier --write"],
};
