# Learn MkDocs / Overview

There is often a need to create an integrated static website to organize documentation, visualizations, etc. and provide navigation between resources.
A static website consists of files that can be generated ahead of time and therefore doesn’t
rely on back-end server programs to query databases or otherwise generate dynamic content.
A static website can include purely static files such as text, HTML, and images,
in which case the web browser simply displays pre-generated content.

The website also can be somewhat dynamic and utilize JavaScript that runs in a web browser to provide a dynamic look, such as interactive maps and graphs.
The data content can be static, or could be refreshed on the server where files are read.
For example, for a real-time application, the web browser application could refresh itself
every few minutes to utilize data files on a server that are updated.
The new content could, for example, be processed on a local computer and updated to
Amazon S3 or other cloud storage as a public website that can be accessed by links in the static website.

The above approaches can involve extensive programming using HTML, CSS, and JavaScript (and all the JavaScript libraries that are available).
However, such programming requires technical skills that many people do not have.
Another approach is to use a framework that processes simple input to create static websites with dynamic features like navigation menus.

MkDocs is a useful documentation tool that processes [Markdown](https://en.wikipedia.org/wiki/Markdown) files into a static website.
The source Markdown files for the website are simple text files and images that can easily be maintained under version control.
For example, text file versions are tracked rather than binary document files such as Microsoft Word.
This approach works well for many simple document formats.

MkDocs software is free and open source and only requires that Python is installed while editing the documentation
(Python is not needed to view the website when deployed to the cloud).
See the [MkDocs documentation](http://www.mkdocs.org/).
The documentation that you are reading was prepared using MkDocs.

The Open Water Foundation recommends using MkDocs for the following purposes:

* Software developer documentation - explain how to set up and use the development environment
* Software user documentation - provide navigable documentation with screen shots and examples
* Project documentation - use navigable website rather than PDF documents so that project content can more easily be a living document
* Process documentation - use navigable website to facilitate understanding process steps at summary and detailed level

## Alternatives to MkDocs

Alternatives to MkDocs should be considered where MkDocs does not satisfy requirements.
Alternatives to MkDocs includes:

* [Sphinx](https://en.wikipedia.org/wiki/Sphinx_(documentation_generator)), which uses reStructuredText source files rather than Markdown.


## Next Steps

The remainder of this documentation describes how to install MkDocs software, set up a MkDocs documentation project,
edit and review documentation, and deploy the documentation to the web.
