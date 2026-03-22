# About

This project is a Python rewrite of [TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET.git) project.

This is a [uv](https://docs.astral.sh/uv/) based project. There is no such thing to run the project in our case as it is just a set of python files. `uv` is used here to format, lint all the files. For running scripts, this project is uses [just](https://github.com/casey/just) script runner.

> [!NOTE] This project is in active development phase. I have prepared a checklist using the files from the [original project](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET.git). You can find that in [`CHECKLIST.md`](CHECKLIST.md)

# Installation

1. First clone the project using:

```bash
git clone https://github.com/devharshthakur/tcs-coding-sheet-py.git
```

2. Run the bun install command to install nodejs dependencies

```bash
bun install 
```

> Note: We use bun only as a package manager. We still use nodejs as runtime

3. Now you can run any file via uv:

```bash
uv run <path_to_the_file>
```

## Contribution

To Contribute to the project please refer [CONTRIBUTING.MD](./CONTRIBUTING.md) and please follow [CODE_OF_CONDUCT](./CODE_OF_CONDUCT.md).

## Resources

- [`CHECKLIST.md`](CHECKLIST.md) for progress tracking
- [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution notes and commit workflow

## License

This project is licensed under the [MIT](./LICENSE) License.
