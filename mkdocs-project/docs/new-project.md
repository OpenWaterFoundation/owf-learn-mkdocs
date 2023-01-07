# MkDocs / New Project #

MkDocs uses a standard folder structure to organize its configuration file and Markdown content files.
The main decisions related to project configuration are to decide how to organize the site's content
in separate pages that are well-organized.

The remainder of this page contains the following sections:

*   [Standard MkDocs Project Files](#standard-mkdocs-project-files)
*   [MkDocs Project Conventions for Git Repository](#mkdocs-project-conventions-for-git-repository)
    +   [MkDocs Project is Only Repository Content](#mkdocs-project-is-only-repository-content) - repository is dedicated to documentation
    +   [MkDocs Project is a Component of Repository](#mkdocs-project-is-a-component-of-repository) - for example, documentation for software product
    +   [Markdown File Recommendations](#markdown-file-recommendations) - to facilitate use with Git
*   [Create New MkDocs Project](#create-new-mkdocs-project)
    +   [Create MkDocs Project from Scratch](#create-mkdocs-project-from-scratch) - useful if no suitable project can be copied
    +   [Copy an Existing MkDocs Project's Files](#copy-an-existing-mkdocs-projects-files) - useful if new documentation is similar to other documentation
*   [Git Repository Configuration Files](#git-repository-configuration-files)
*   [Next Steps](#next-steps)

----------------

## Standard MkDocs Project Files

The MkDocs "project" consists of the following:

*   `mkdocs.yml` configuration file listing the Markdown files that are a part of the website, and other configuration properties.
    +   For example, see the [repository `mkdocs.yml`](https://github.com/OpenWaterFoundation/owf-learn-mkdocs/blob/master/mkdocs-project/mkdocs.yml)
        file for this documentation.
    +   Markdown files must be listed in this file in order to be processed into website HTML content.
        If they are not listed, then a link to the file will return no content because the Markdown will
        not have been converted to HTML.
        This presents challenges for complex documents because a long list of files will be used and
        the navigation features for a MkDocs theme may not handle the long list well.
        For example, some themes do not have collapsable navigation menus and the long list of files will require vertical
        scrolling for navigation or horizontal menus will overflow the page heading.
        Themes are discussed in the [Edit Content](edit.md) section).
        The MkDocs software will print to the console a list of missing files and broken links.
*   `docs/` folder containing Markdown files, images, and other content.
    +   Folders can be used for content sections
    +   Folders can be used for linked files such as images and examples.
*   `site/` folder that will be generated containing the static website content.
    +   Contents can be copied to a cloud location to publish the website.
    +   MkDocs creates the website in memory during editing/viewing sessions so use `mkdocs build` to force
        creating the `site` folder.
*   Other folders can be used for scripts to automate processing and prepare the output for deployment,
    for example the [`build-util` scripts](https://github.com/OpenWaterFoundation/owf-learn-mkdocs/tree/master/build-util)
    used in the repository for this documentation.

The MkDocs documentation is straightforward and provides examples of the `mkdocs.yml` configuration file.
See [Writing your docs in the MkDocs documentation](http://www.mkdocs.org/user-guide/writing-your-docs/).

## MkDocs Project Conventions for Git Repository ##

It is common that a MkDocs project will reside in a repository in order to track versions of documentation file content.
This documentation focuses on conventions for Git version control system,
but the information would be similar for other version control systems.

The repository may only contain documentation (similar to this documentation) or
the repository may contain software or other files and the MkDocs project is a secondary component.
The following sections provide recommendations for organizing files in the repository for both cases.
It is assumed that the repository folder already exists, for example due to cloning the repository from GitHub,
Bitbucket, or other cloud location.

### MkDocs Project is Only Repository Content ###

In this case the repository only contains documentation and the MkDocs environment is the primary concern.
For the following example, the repository for this documentation is named `owf-learn-mkdocs`.
When cloned from GitHub, a folder will be created with the same name.
Rather than assign unique names to each MkDocs project,
it is recommended to simply use `mkdocs-project` for the name, which will result in the following file structure.
This clearly indicates that a MkDocs project can be found in `mkdocs-project`.

```text
some-parent-folder/        The parent folder where the Git repository was cloned.
  owf-learn-mkdocs/        Git repository folder, under which resides .git, etc.
    README.md              As per GitHub, etc. conventions.
    .gitattributes         As per Git conventions.
    .gitignore             As per Git conventions, remember to ignore mkdocs-project/site/.
    build-util/            See Deploy Website section of this documentation.
    mkdocs-project/        MkDocs project location, under which are all MkDocs files.
      mkdocs.yml           MkDocs project configuration file.
      docs/                Folder where Markdown and other content files exist.
        *.md 
      site/                Folder automatically created by MkDocs software.
        index.html         Default landing page for static website.
        many other files
```

The above convention ensures that whenever a `mkdocs-project` folder is found in a repository,
it should be obvious that a MkDocs project is present.
Every file under the `mkdocs-project` folder will adhere to MkDocs conventions and other files can be added outside of these files,
for example to upload the website to a cloud location.

See [Create New MkDocs Project](#create-new-mkdocs-project) below for instructions on creating the above files.

### MkDocs Project is a Component of Repository ###

A modification to the recommendations in the previous section can be used in cases
when the MkDocs static website is a component of a repository.
Most software repositories will have a folder `src` for source code.
It is recommended to create one or more MkDocs project folders parallel to the `src` folder, for example:

*   `doc-admin-mkdocs-project` - for adminstrator documentation, for example to install/deploy and configure software
*   `doc-dev-mkdocs-project` - for developer documentation, for example, to be used by software developers
*   `doc-user-mkdocs-project` - for user documentation, to be used by software users after software is installed

The files under the above folders should be similar to the previous section, for example where `mkdocs-project` (previous section) is
equivalent to `doc-dev-mkdocs-project` (below):

```text
some-parent-folder/           The parent folder where the Git repository was cloned.
  some-git-repo-folder/       Git repository folder, under which resides .git, etc.
    README.md                 As per GitHub, etc. conventions.
    .gitattributes            As per Git conventions.
    .gitignore                As per Git conventions, remember to ignore doc-dev-mkdocs-project/site.
    doc-dev-mkdocs-project/   Folder dedicated to a MkDocs project for developer documentation.
      build-util/             See Deploy Website section of this documentation.
      mkdocs.yml              MkDocs project configuration file.
      docs/                   Folder where Markdown and other content files exist.
        *.md 
      site/                   Folder automatically created by MkDocs software.
        index.html            Default landing page for static website.
        many other files
    src/                      Source code files in software project.
```

See [Create New MkDocs Project](#create-new-mkdocs-project) below for instructions on creating the above files.

## Markdown File Recommendations ##

Markdown files are text files and therefore are easily managed in Git.
However, the following are general recommendations.

1.  **Break content into relatively small lines** - It is possible with text editors to lose track of
    text file formatting, which can result in long lines.
    Editors automatically wrap content so it may be difficult to know where line breaks exist in files.
    Long lines make it difficult to use `git diff` and other file comparison tools because a
    change within a line may be buried within the long line and requiring scrolling to detect differences.
    To make it easier to view changes, break content into shorter lines,
    for example by inserting line breaks (`Enter` key on keyboard) after commas, periods, and other punctuation.
    A manageable line line length is ~80 characters or less.
2.  **Use `.gitattributes` file to handle line breaks** - The `* text=auto` line in the
    `.gitattributes` file ensures that the repository will store text files with Linux-style
    line breaks (NL) and use native operating system line breaks (NL on Linux, CRNL on Windows).
    This will ensure that all content is stored consistently in the repository,
    regardless of the operating system used to edit the content.
    See the [`.gitattributes` file](#gitattributes-file) section for more information.
3.  **Do not mix development environments on a computer.** - There are issues if
    content is edited in Cygwin and Git Bash on the same computer,
    because of the ways that line breaks and executable file permissions are handled.
    Therefore, pick an environment and use it consistently for editing content.
    If Git commands print irritating warnings about line endings, it is a clue that an environment
    other than that used for the repository clone is being used.
 
## Create New MkDocs Project ##

There are two primary ways to start a new MkDocs project,
both of which will result in a file structure similar to that described in previous sections.

### Create MkDocs Project from Scratch ###

To create a MkDocs project from scratch, change to the repository folder and run the following command from a command shell.
For example, for a documentation-only repository:

```sh
$ mkdocs new mkdocs-project
INFO    -  Creating project directory: mkdocs-project
INFO    -  Writing config file: mkdocs-project\mkdocs.yml
INFO    -  Writing initial docs: mkdocs-project\docs\index.md
```

And for a documentation component in a software project:

```sh
$ mkdocs new doc-dev-mkdocs-project
INFO    -  Creating project directory: doc-dev-mkdocs-project
INFO    -  Writing config file: doc-dev-mkdocs-project\mkdocs.yml
INFO    -  Writing initial docs: doc-dev-mkdocs-project\docs\index.md
```

This will create template `mkdocs.yml` and `docs/index.html` files.
The files then need to be edited to configure website organization and content.
The top-level folder can be renamed after creation, as needed.

### Copy an Existing MkDocs Project's Files ###

Creating a MkDocs project from scratch as described in the previous section does not do much work.
Consequently, it may be easier to copy and modify an existing MkDocs project.
To do so, manually create the `mkdocs-project` folder (or use a different name as appropropriate)
under the repository folder and copy files from another MkDocs project,
in particular the `mkdocs.yml` configuration file.
Manually create (or copy) the `docs/` folder and any files that should serve as the starting point for the new MkDocs project content.
Manually create (or copy) other files such as Git configuration files and `build-util` scripts.

Edit the files to configure the website organization and content.
Make sure to clean up files before committing to the repository to avoid confusion with irrelevant files.

## Git Repository Configuration Files ##

The following are basic examples of Git repository configuration files that should be included with the documentation files.

### `.gitignore` File ###

In the main Git repository folder, include a `.gitignore` file to avoid committing temporary files from text editors.
See also the [.gitignore documentation](https://git-scm.com/docs/gitignore).


```text
# Ignore the following files (do not commit working files to repository)

# Ignore temporary files from editors

# vi/vim
*.swp
*.swo

# Ingore the dynamic MkDocs site folder

mkdocs-project/site/

# Office temporary files

*.tmp

# Word
#~$*.doc*
# Excel
#~$*.xls*
# PowerPoint
#~$*.ppt*
~$*

```

### `.gitattributes` File ###

In the main Git repository folder, include a `.gitattributes` file to ensure that text files are saved with newline characters
and checked-out files use the operating system end of line.
See also the [.gitattribues documentation](https://git-scm.com/docs/gitattributes).

```text
# Settings for the repository

# Cause line endings in the repository to be newline (\n) and local files to be that of the operating system,
# LF for Linux and Mac and CRLF for Windows.

* text=auto

# Denote binary files

*.png binary
*.jpg binary
```

## Next Steps ##

Next, [configure the project](config.md) and [edit the content](edit.md).
