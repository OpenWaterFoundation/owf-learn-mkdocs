# MkDocs / Troubleshooting #

This documentation provides information to troubleshoot Markdown.

*   [Introduction](#introduction)
*   [Troubleshooting a Hosted Web Site](#troubleshooting-a-hosted-web-site)
    +   [Web page does not show updates after uploading files](#web-page-does-not-show-updates-after-uploading-files)
*   [Troubleshooting Markdown](#troubleshooting-markdown)
    +   [Link - Source Markdown is shown instead of the link](#link-source-markdown-is-shown-instead-of-the-link)
    +   [List - Levels use the same symbol](#list-levels-use-the-same-symbol)
    +   [List - Numbers restart](#list-numbers-restart)
    +   [Table - Source Markdown is shown instead of the formatted table](#table-source-markdown-is-shown-instead-of-the-formatted-table)

-----------------

## Introduction ##

Markdown is a simple documentation format with a limited number of formatting elements.
Consequently, it is relatively easy to convert Markdown into other formats that
are rendered in software, such as HTML shown in a web browser.
However, different software tools may implement Markdown differently,
and the various Markdown "flavors" (such as GitHub-flavored Markdown) and plugins may also cause issues.

This documentation provides troubleshooting recommendations for common issues,
in particular those experienced when using MkDocs.
See also the [Edit](edit.md) documentation for tips on editing Markdown content.

## Troubleshooting a Hosted Web Site ##

A website created with MkDocs is typically uploaded to the cloud to be hosted as a static website,
for example using Amazon S3 and CloudFront.
The following are common web site issues.

### Web page does not show updates after uploading files ###

Uploading a website to the cloud may not show the updated content when viewed in a web browser,
even after refreshing the page.  The following are possible solutions:

1.  Make sure that the content is updated in the server's cache.
    For example, if using Amazon Web Services S3 and CloudFront,
    make sure that the files are invalidated in the CloudFront distribution.
2.  It may be necessary to do a hard refresh in the web browser using ***Ctrl F5***,
    in particular to refresh CSS files such as the custom MkDocs CSS file.

## Markdown Problems ##

The following are common problems.
The content is grouped according to the element type.

### Link - Source Markdown is shown instead of the link ###

If the source Markdown is shown instead of the desired link text:

1.  Check that the URL does not contain a space or other non-text characters.
    If necessary, use
    [percent-encoded characters](https://en.wikipedia.org/wiki/Percent-encoding)
    such as replacing a space with `%20`.
    If possible, it is often best to use folders and file names that do not include spaces.

### List - Levels use the same symbol ###

If an unordered list (bullet list) uses the same symbol for multiple levels:

1.  Try changing the MkDocs custom CSS.
    See the [Custom CSS Configuration](edit.md#custom-css-configuration) documentation.

### List - Numbers restart ###

If the numbers in a numbered list restart rather than continuing sequentially,
it is often an issue with indentation.

1.  See the [List - Ensuring incremental numbers](edit.md#list-ensuring-incremental-numbers) documentation.

### Table - Source Markdown is shown instead of the formatted table ###

If a Markdown table shows the original Markdown rather than the expected format:

1.  Make sure that the number of columns in the heading line match the number of separators (line under the column headings).
2.  Make sure that there is not a space or other stray characters after the last column's content.
    For example, use a text editor to search for `|` followed by a space.
