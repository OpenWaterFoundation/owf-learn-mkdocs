# MkDocs / Overview

There is often a need to create an integrated static website to organize documentation or other content
and provide navigation between resources.
A static website consists of files that can be generated ahead of time and therefore doesn’t
rely on back-end server programs to query databases or otherwise generate dynamic content.
A static website can include purely static files such as text, HTML, and images,
in which case the web browser simply displays pre-generated content.
Links can be included in static website content to access dynamic content, as needed.

MkDocs is a useful documentation tool that processes [Markdown](https://en.wikipedia.org/wiki/Markdown) files into a static website
(see also [Markdown in Resources section](resources.md).
The source Markdown files for the website are simple text files and images that can easily be maintained under version control.
For example, text file versions are tracked rather than binary document files such as Microsoft Word.
This approach works well for many documents that benefit from navigation and web integration.

MkDocs software is free and open source and only requires that Python is installed while editing the documentation
(Python is not needed to view the website when deployed to the cloud).
See the [MkDocs documentation](http://www.mkdocs.org/).
The documentation that you are reading was prepared using MkDocs.

The Open Water Foundation recommends using MkDocs for the following purposes:

*   ***Software developer documentation*** - explain how to set up and use the development environment
*   ***Software user documentation*** - provide navigable documentation with screen shots and examples
*   ***Project documentation*** - use navigable website rather than PDF documents so that project content can more easily be a living document
*   ***Process documentation*** - use navigable website to facilitate understanding process steps at summary and detailed level

## Alternatives to MkDocs

Alternatives to MkDocs should be considered where MkDocs does not satisfy requirements.
Alternatives to MkDocs includes:

*   [Sphinx](https://en.wikipedia.org/wiki/Sphinx_(documentation_generator)), which uses reStructuredText source files rather than Markdown.
*   GitHub pages or other cloud-hosted content that is integrated with version control.


## Next Steps

The remainder of this documentation describes how to install MkDocs software, set up a MkDocs documentation project,
edit and review documentation, and deploy the documentation to the web.
