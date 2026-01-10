# Contributing

Contributions of all kinds are welcome here, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Example Contributions

You can contribute in many ways, for example:

- [Contributing](#contributing)
  - [Example Contributions](#example-contributions)
    - [Report Bugs](#report-bugs)
    - [Fix Bugs](#fix-bugs)
    - [Implement Features](#implement-features)
    - [Write Documentation](#write-documentation)
      - [Documentation Style](#documentation-style)
    - [Submit Feedback](#submit-feedback)
  - [Get Started!](#get-started)
    - [Pull Request Guidelines](#pull-request-guidelines)

### Report Bugs

Report bugs at https://github.com/UBC-MDS/geospatial_toolkit/issues.

**If you are reporting a bug, please follow the template guidelines. The more
detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and
`help wanted` is open to whoever wants to implement it. When you decide to work on such
an issue, please assign yourself to it and add a comment that you'll be working on that,
too. If you see another issue without the `help wanted` label, just post a comment, the
maintainers are usually happy for any support that they can get.

### Implement Features

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement it. As
for [fixing bugs](#fix-bugs), please assign yourself to the issue and add a comment that
you'll be working on that, too. If another enhancement catches your fancy, but it
doesn't have the `help wanted` label, just post a comment, the maintainers are usually
happy for any support that they can get.

### Write Documentation

geospatial-toolkit could always use more documentation, whether as
part of the official documentation, in docstrings, or even on the web in blog
posts, articles, and such. Just
[open an issue](https://github.com/UBC-MDS/geospatial_toolkit/issues)
to let us know what you will be working on so that we can provide you with guidance.

#### Documentation Style

We use the NumPy docstring format for all functions. Ensure every function includes:

- A clear summary line.
- Parameters with type hints.
- Returns with types.
- Raises for error handling.
- Examples using doctest format.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/UBC-MDS/geospatial_toolkit/issues. If your feedback fits the format of one of
the issue templates, please use that. Remember that this is a volunteer-driven
project and everybody has limited time.

## Get Started!

Ready to contribute? Here's how to set up geospatial-toolkit for
local development.

1. Clone the repository from the UBC-MDS organization:

    ```shell
    git clone git@github.com:UBC-MDS/geospatial_toolkit.git
    ```

2. [Install hatch](https://hatch.pypa.io/latest/install/).

3. Create a branch for local development using the `dev` branch as a starting point. We follow a `feature/feature-name` or `fix/bug-name` naming convention.

    ```shell
    git checkout dev
    git pull origin dev
    git checkout -b feature/name-of-your-feature
    ```

    Now you can make your changes locally.

4. When you're done making changes, apply the quality assurance tools and check
   that your changes pass our test suite using hatch. 

    ```shell
    hatch run test:run
    ```

5. Commit your changes and push your branch to GitHub. Please use [semantic
   commit messages](https://www.conventionalcommits.org/).

    ```shell
    git add .
    git commit -m "feat: summarize your changes"
    git push -u origin feature/name-of-your-feature
    ```

    Examples of semantic commits:

    - `feat: add haversine distance calculation`
    - `docs: update readme with ecosystem summary`
    - `fix: correct latitude range validation`
    - `chore: update pyproject.toml dependencies`

6. Open the link displayed in the message when pushing your new branch in order
   to submit a pull request.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.
3. Your pull request will automatically be checked by the full test suite.
   It needs to pass all of them before it can be considered for merging.
4. Every pull request must be reviewed and approved by at least one other team member before it can be merged into the dev branch.
5. Link the pull request to its corresponding issue by including "Closes #X" or "Fixes #X" in the PR description. This ensures the project board stays updated.
