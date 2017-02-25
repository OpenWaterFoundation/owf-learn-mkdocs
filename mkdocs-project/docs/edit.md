# Learn MkDocs / Edit Content

Website content can be created after installing the software and initializing a new MkDocs project.

The MkDocs documentation is straightforward and provides examples of content.
See the following resources to help with formatting content:

* [Writing your docs](http://www.mkdocs.org/user-guide/writing-your-docs/)
* [Adam Prichard's Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

This documentation contains the following sections:

* [Selecting a Theme](#selecting-a-theme) - used to customize look and feel of website
* [Starting Local Web Server to Review Content](#starting-local-web-server-to-review-content)
* [MkDocs Examples](#mkdocs-examples) - useful examples and tips

## Selecting a Theme

Experience has shown the following:

* Trying different themes is helpful but having many documents can overwhelm some of the themes.
The "Read the Docs" theme seems to handle many documents.
* Use a multi-level layout for documents when the number of documents starts to grow.
Otherwise readers may not follow the content organization.

## Starting Local Web Server to Review Content

The MkDocs software converts the Markdown files into a static website that uses HTML, CSS, JavaScript, images, and other files.
The conversion of Markdown files to static website content takes place in two ways:

1. In memory when a local MkDocs web server is run  with `mkdocs serve` (no output files are generated).
2. As files when `mkdocs build` is run.

During normal editing, content can be viewed by opening a terminal window and starting the server, for example on Linux:

```
$ cd mkdocs-project
# Takes over window
$ mdocs serve
# Run in background
$ mdocs serve&
```

Then view the website by opening the following link in a web browser:  `http://localhost:8000`

To kill the server, enter Ctrl-C in the terminal.  Only one MkDocs server can run at the same time.

The MkDocs server will scan for changed files and will regenerate the website content.
The web browser will automatically refresh but it may be necessary to manually refresh the page.

## MkDocs Examples

### Link to  a Markdown file in the same folder (does not seems to require file extension):

```text
[text for visible link](other-markdown-file)

```

### Link to a heading in Markdown file in a different folder

Use the following syntax to link to a heading in a separate file, where the words in parenthesis match the
`#` heading.  This is useful for creating internal table of contents to help with navigation.
The following are rules for specifying the reference location in parentheses:

* Start the location name with a `#`.
* Replaces spaces by dash.
* Remove periods and some other special characters as necessary to make the link work.
* Use all lowercase in the reference name.

```text
[text for visible link](../parallel-folder/other-markdown-file#heading-words)

```

### Link to a named location that is not a section heading

It can be useful to include a link to a point within a Markdown file without referring to a heading.
To do so, add the following to create a named location:

```text
1. <a name="step1"></a>Some text for step 1 in a process.
```

Then add a link to the named location similar to the following:

```text
Press "back" in the browser to return to the list of setup steps or [click here](#step1)`
```

### Include language indicator for more specific formatting:

``````
```sh
# Some script
cd someDir
ls -la
```
``````

The following provides a list of languages supported by Markdown, although support will vary by tool:

* [GitHub Markdown language file](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)
* [Languages Supported by Github Flavored Markdown](http://www.rubycoloredglasses.com/2013/04/languages-supported-by-github-flavored-markdown/) - warning, profanity
