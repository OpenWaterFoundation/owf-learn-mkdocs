# Learn MkDocs / Edit

Website content can be created after installing the software and initializing a new MkDocs project.

The MkDocs documentation is straightforward and provides examples of content.
See the following resources to help with formatting content:

* [Writing your docs](http://www.mkdocs.org/user-guide/writing-your-docs/).
* [Adam Prichaard's Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

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
$ mdocs serve
```

Then view the website by opening the following link in a web browser:  `http://localhost:8000`

To kill the server, enter Ctrl-C in the terminal.  Only one MkDocs server can run at the same time.

The MkDocs server will scan for changed files and will regenerate the website content.
The web browser will automatically refresh but it may be necessary to manually refresh the page.

## MkDocs Examples

Reference a Markdown file in the same folder (does not seems to require file extension):

```
[some text](other-markdown-file)

```

Reference a section in Markdown file in a parallel folder (does not seems to require file extension):

```
[some text](../parallel-folder/other-markdown-file#section-name-spaces-replaced-by-dashes)

```

Include language indicator for more specific formatting:

``````
```sh
# Some script
cd someDir
ls -la
```
``````

The following provides a list of languages supported by Markdown, although support will vary by tool (see `ace_mode` ?):

* [GitHub Markdown language file](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)
* [Languages Supported by Github Flavored Markdown - warning profanity](http://www.rubycoloredglasses.com/2013/04/languages-supported-by-github-flavored-markdown/)
