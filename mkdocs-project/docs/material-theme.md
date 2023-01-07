# MkDocs / Material Theme #

This documentation uses the Material theme with MkDocs.  See

*   [Material Theme website](https://squidfunk.github.io/mkdocs-material/)

The following provide guidance for using the Material theme:

*   [Installing Material Theme](#istalling-material-theme)
*   [Specifying Material Theme](#specifying-material-theme)
*   [Configuring Material Theme](#configuring-material-theme)
    +   [Specifying the Favicon](#specifying-the-favicon)
    +   [Enabling Google Analytics](#enabling-google-analytics)

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

1.  Create a `favicon.ico` file.  Any filename can be used (does not need to be `favicon`).
    MkDocs will configure the main `index.html` page to use the favicon and may rename the file.
    Favicon files can be `.ico` or `.png` format.
    For example use Gimp software to create a 32x32 pixel image and save with an `ico` file extension.
2.  Save the file in a folder under `docs`, for example `docs/img` or `docs/images` in the MkDocs project folder.
3.  Specify configuration information in the `mkdocs.yml` file, similar to the following:

```
theme:
  name: 'material'
  favicon: 'img/favicon.ico'
```

The favicon may not be shown when viewing the documentation locally but should be visible when deployed to the web.

### Enabling Google Analytics ###

Google Analytics can be enabled for a MkDocs site to track visits to each page.

#### Google Analytics 4 Property ####

A Google Analytics 4 property can be configured using the Material theme configuration properties. See:

*   [Setting up site analytics](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-analytics/)

The MkDocs configuration properties are similar to the following:

```
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

#### Google Analytics Universal Property ####

**The Universial property is an older technology.
The Google Analytics 4 Property should be used instead.**

See the previous section for newer versions of Material theme.
The following is older syntax.

Enabling Google Analytics is useful for tracking page hits.
However, ad blockers may disable Google Analytics, and therefore tracking data will be less than 100% of actual.
The MkDocs Material theme supports Google Analytics integration (see the
[Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/getting-started#google-analytics/)).
The following is an example of MkDocs configuration file properties to enable Google Analytics,
where the appropriate tracking ID needs to be specified.
The static website pages created by MkDocs will contain Google Analytics JavaScript code.

```
google_analytics:
  - 'UA-XXXXXXXX-X'
  - 'auto'
```
