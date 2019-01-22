# owf-learn-mkdocs #

This repository contains the [Open Water Foundation (OWF)](http://openwaterfoundation.org/) MkDocs training materials,
which provides guidance for implementing MkDocs projects for software and other documentation.
The documentation is written for the layperson in order to encourage use of MkDocs.

See the deployed [OWF / Learn MkDocs](http://learn.openwaterfoundation.org/owf-learn-mkdocs/) documentation.

## Repository Contents ##

The repository contains the following:

```text
.github/              Files specific to GitHub such as issue template.
.gitattributes        Typical Git configuration file.
.gitignore            Typical Git configuration file.
README.md             This file.
build-util/           Useful scripts to view, build, and deploy documentation.
mkdocs-project/       Typical MkDocs project for this documentation.
  mkdocs.yml          MkDocs configuration file for website.
  docs/               Folder containing source Markdown and other files for website.
  site/               Folder created by MkDocs containing the static website - ignored using .gitignore.

```

## Development Environment ##

The development environment for contributing to this project requires installation of Python, MkDocs, and Material MkDocs theme.
Python 3 has been used for development.  See the [`mkdocs-project/docs/install.md`](mkdocs-project/docs/install.md)
file for information about installing these tools.

## Editing and Viewing Content ##

If the development environment is properly configured, edit and view content as follows:

1. Edit content in the `mkdocs-project/docs` folder and update `mkdocs-project/mkdocs.yml` as appropriate.
2. Run the `build-util/run-mkdocs-serve-8000.sh` script (Cygwin/Linux) or equivalent.
3. View content in a web browser using URL `http://localhost:8000`.

## License ##

The OWF Learn MkDocs website content and examples are licensed under the
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0).

## Contributing ##

Contribute to the documentation as follows:

1. Use GitHub repository issues to report minor issues.
2. Use GitHub pull requests.

## Release Notes ##

The following release notes indicate the update history for documentation, with GitHub repository issue indicated,
if applicable (links to issues via README.md are not cleanly supported by GitHub so use the repository issues page to find).

* 2019-01-22 [7] - update documentation to focus on Python 3 and MkDocs 1+
* 2017-11-29 [6] - add examples for formatting Markdown literally and controlling table column width
* 2017-10-21 [2,3,4] - cleanup theme documentation, add issue template.
* 2017-10-20 [1] - switch to Material theme, update documentation based on experience.
* 2017-08-07 - switch to Cosmo theme, update documentation based on experience.
