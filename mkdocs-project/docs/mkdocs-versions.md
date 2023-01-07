# MkDocs / Version Differences #

MkDocs is generally consistent in its behavior.
However, the following information summarizes major differences between versions.
See also the [MkDocs release notes](https://www.mkdocs.org/about/release-notes/) and release notes for the theme that is used.
It may also be helpful to search the
[MkDocs GitHub issues](https://github.com/mkdocs/mkdocs/issues) to troubleshoot unexpected behavior.

*   [Version 1](#version-1)
*   [Version 0](#version-0)

-----------------

## Version 1 ##

Version 1 made a few major changes that may impact source documentation files and project configuration.

*   File and link specification:
    +   `use_directory_urls: true` is the default
        -   This causes URLs to end in `/` rather than a `.html` file. 
        -   [See the documentation](https://www.mkdocs.org/user-guide/configuration/#use_directory_urls)
        -   **This may cause old documentation to have broken links,
            especially if the next item is also an issue.**
    +   To make internal links work, must specify `.md` in filenames whereas previously the extension could be omitted.
        This may be related to the above change.
    +   See also console messages that are printed by `mkdocs`, which alert to missing and extra files.
*   Changes to `mkdocs.yml` configuration file:
    +   Change `pages` to `nav`. 
    +   See [reference to `mkdocs.yml` file](https://www.mkdocs.org/user-guide/configuration/) for supported properties.

## Version 0 ##

MkDocs was at version 0 for a long time.
A lot of documentation may have been written that needs to be updated to version 1 (see above).
