# Learn MkDocs / Edit Content #

Website content pages are created/edited with a text editor.
Each markdown file that is created should be included in the `mkdocs.yml` configuration file so that the MkDocs
software can process from Markdown into final form.

The MkDocs documentation is straightforward and provides examples of content.
See the following MkDocs and Markdown resources to help with formatting content.
Additionally, because Markdown is text, one of the best ways to learn is to view the source files
for a Markdown document.
For example, [view the source files for this documentation on GitHub](https://github.com/OpenWaterFoundation/owf-learn-mkdocs).

* [Writing your docs](http://www.mkdocs.org/user-guide/writing-your-docs/)
* [Mastering Markdown on GitHub](https://guides.github.com/features/mastering-markdown/)
* [Adam Prichard's Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

The remainder of this page contains the following sections:

* [Selecting a Theme](#selecting-a-theme) - used to customize look and feel of website
	+ [Installing Third-Party MkDocs Theme](#installing-third-party-mkdocs-theme)
* [Starting Local Web Server to Review Content](#starting-local-web-server-to-review-content)
	+ [Stopping MkDocs Web Server](#stopping-mkdocs-web-server)
* [Selecting File Naming Convention](#selecting-file-naming-convention)
* [Selecting Markdown Documentation Styles](#selecting-markdown-documentation-styles)
* [MkDocs Markdown Examples](#mkdocs-markdown-examples) - useful examples and tips
	+ [Link to  a Markdown file in the same or different folder](#link-to-a-markdown-file-in-the-same-or-different-folder)
	+ [Link to a heading in Markdown file](#link-to-a-heading-in-markdown-file)
	+ [Link to a named location that is not a section heading](#link-to-a-named-location-that-is-not-a-section-heading)
	+ [Include language indicator for more specific formatting](#include-language-indicator-for-more-specific-formatting)

-----------------

## Selecting a Theme ##

The `mkdocs.yml` file allows a theme to be specified, which controls the look and feel of the website:

```yaml
theme: readthedocs
```

Changing the theme involves installing the theme files and changing the configuration file.

Experience has shown the following:

* The default themes shipped with MkDocs (`readthedocs` and `mkdocs`) are generally adequate but have limitations,
especially for larger sites.
In particular, the navigation features are limited.
* Sites having many documents can cause the left navigation bar to get very long, for example in `readthedocs` theme.
* A menu-based theme with many menus can cause the page header to overflow and overwrite the top of pages - it is
typically necessary in this case to limit the number of menus or words in menus in order to fit the maximum
page width.
* Some themes provide search features and some do not.  If a search feature is desirable then make sure to check the theme.

Overcoming these issues requires experimenting with themes and perhaps adding custom CSS configuration.
It may also be desirable to customize the branding of documentation, which involves adding favicon and editing the CSS.

***Based on experimentation, the Material theme has been selected for this and other documentation.***
The Material theme provides search features, navigation for the entire site (left navigation panel) and
navigation within a page (right navigation panel).
This documentation uses the Material theme.

### Installing Third-Party MkDocs Theme ###

If it is desired to use a MkDocs theme other than those distributed with MkDocs, first review available themes, for example:

* [MkDocs Themes on GitHub](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)
* [Material Theme](http://squidfunk.github.io/mkdocs-material/)
* [MkDocs Bootswatch Project Themes on GitHub](http://mkdocs.github.io/mkdocs-bootswatch/)

To use a third-party theme, follow the link for the theme on the above page and follow installation instructions.
Note that in some cases the theme will already have been installed and `pip` will indicate that update can be used.

After installing the theme, change the `theme` configuration property in the `mkdocs.yml` file to indicate the new theme.
It may be necessary to and restart MkDocs (see next section).

## Starting Local Web Server to Review Content ##

The MkDocs software converts the Markdown files into a static website that uses HTML, CSS, JavaScript, images, and other files.
The conversion of Markdown files to static website content takes place in two ways:

1. In memory when a local MkDocs web server is run  with `mkdocs serve` (no output files are generated in the `site` folder).
2. As files in the `site` folder when `mkdocs build` is run.

During normal editing, a text editor is used to edit the Markdown files.
Once a file is saved, the content can be viewed in a browser using a local web server provided by MkDocs.
To start the server, open a terminal window and execute the following commands.

```sh
cd mkdocs-project
mkdocs serve
```

Then view the website by opening the following link in a web browser:  `http://localhost:8000`.

The MkDocs server will scan for changed files and will regenerate the website content.
The web browser will automatically refresh but in some cases it may be necessary to manually refresh the page.

The server will not refresh content if, for example, a new entry has been made in the `mkdocs.yml` file
but the referenced file does not yet exist.
In this case, create a basic file so that the server is not impacted by a missing file.

It is often helpful to use a script to document how to run processes.
The following [`run-mkdocs-serve-8000.sh`](https://github.com/OpenWaterFoundation/owf-learn-mkdocs/tree/master/build-util/run-mkdocs-serve-8000.sh)
script for Cygwin and Linux illustrates how to run the MkDocs server on a port 8000 (the default).
A similar script could be used to run on a specific port,
which is useful when multiple servers need to be run at the same time.

```sh
#!/bin/sh
#
# Run mkdocs serve on port 8000 (default)

# Make sure that this is being run from the build-util folder
pwd=`pwd`
dirname=`basename ${pwd}`
if [ ! ${dirname} = "build-util" ]
        then
        echo "Must run from build-util folder"
        exit 1
fi

cd ../mkdocs-project

echo "View the website using http://localhost:8000"
#mkdocs serve -a 0.0.0.0:8000
mkdocs serve

```

### Stopping MkDocs Web Server ###

To stop the MkDocs web server, enter `Ctrl-C` in the command shell.  Only one MkDocs server can run at the same time for a port number.

## Selecting File Naming Convention ##

The Markdown files should follow a naming convention that facilitates maintaining the content,
for example:

* Use consistent convention such as all lowercase with dashes separating words, for example `deploy-website` (folder)
and `deploy-website.md` (Markdown file).
* If images are used, create a folder such as `pagename-images`, where `pagename` is the name of the content page and
the indicated folder is the images for that page.

It is possible that other documentation will link to a page so some care should be taken not to frequently change filenames.

## Selecting Markdown Documentation Styles ##

One of the benefits of using Markdown, MkDocs, and MkDocs theme is that styles are defaulted.
For example, using the `#` headings will result in a font style.
However, there is still a need to decide how Markdown will be applied to format a document.
It is possible to customize the MkDocs theme that is used to control such styles.
Another styling approach is to decide how to use basic Markdown to format documentation.
For example, the following may be selected as a convention for styling:

* Indicate all user input with triple-backticks using appropriate content type.
* Indicate all inline text program names with surrounding single-backticks.
* Use italic bold (three surrounding asterisks) for software labels/features such as buttons to click.

Other choices can be made to ensure consistency in the documentation.

## MkDocs Markdown Examples ##

The following are useful examples and tips determined through use of MkDocs.

### Link to a Markdown file in the same or different folder ###

A Markdown file can be linked to in the same folder by using the link notation.
In this case the name of the markdown file without `.md` is specified in parentheses.

```text
[text for visible link](other-markdown-file)
```

If the file exists in a different folder, specify a leading path:

```text
[text for visible link](../some-folder/other-markdown-file)
```

### Link to a heading in Markdown file ###

Use the following syntax to link to a heading in a separate file, where the words in parenthesis match the
`#` heading.  This is useful for creating internal table of contents to help with navigation.
The following are rules for specifying the reference location in parentheses:

* Start the location name with a `#`.
* Replace spaces by dash.
* Remove periods and some other special characters as necessary to make the link work.
* Use all lowercase in the location name.

```text
[text for visible link](../parallel-folder/other-markdown-file#heading-words)

```

If the link is to a location in the current file, omit the leading filename and start the reference with `#`.

### Link to a named location that is not a section heading ###

It can be useful to include a link to a point within a Markdown file without referring to a heading.
To do so, add the following to create a named location:

```text
1. <a name="step1"></a>Some text for step 1 in a process.
```

Then add a link to the named location similar to the following:

```text
Press "back" in the browser to return to the list of setup steps or [click here](#step1)`
```

### Include language indicator for more specific formatting ###

It is useful to automatically format content based on the language for the content.
For example, the following uses notation <code>```sh</code> to indicate that the content is for a Linux shell script:

```sh
# Some script
cd someDir
ls -la
```

The following provides a list of languages supported by Markdown, although support will vary by tool:

* [GitHub Markdown language file](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)
* [Languages Supported by Github Flavored Markdown](http://www.rubycoloredglasses.com/2013/04/languages-supported-by-github-flavored-markdown/) - warning, profanity
