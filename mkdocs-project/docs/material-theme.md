# MkDocs / Material Theme #

This documentation uses the Material theme with MkDocs.  See

* [Material Theme website](https://squidfunk.github.io/mkdocs-material/)

The following provide guidance for using the Material theme:

* [Installing Material Theme](#istalling-material-theme)
* [Specifying Material Theme](#specifying-material-theme)
* [Configuring Material Theme](#configuring-material-theme)
	+ [Specifying the Favicon](#specifying-the-favicon)

-----------------

## Installing Material Theme ##

See the [Install MkDocs](install.md) section for instructions for installing the Material theme.

## Specifying Material Theme ##

To specify the Material theme, include the following in the `mkdocs.yml` file:

```yaml
theme:
  name: material
```

## Configuring Material Theme ##

The Material theme can be configured using information on the
[Material theme website Getting Started page](https://squidfunk.github.io/mkdocs-material/getting-started/).

Below are some specific configuration topics that may be useful.

### Specifying the Favicon ###

A favicon icon is the image used for the browser tab when the documentation is loaded.
Mkdocs provides general guidance for specifying a favicon.
However, the Material theme has its own
[favicon configuration approach described here](https://squidfunk.github.io/mkdocs-material/getting-started/#favicon).

To specify a favicon:

1. Create a `favicon.ico` file.  For example use Gimp software to create a 32x32 pixel image and save with an `ico` file extension.
2. Place the file in the `docs/img` folder in the MkDocs project folder.

The favicon may not be shown when viewing the documentation locally but should be visible when deployed to the web.
