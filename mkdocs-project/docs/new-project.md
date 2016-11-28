# Learn MkDocs / New MkDocs Project

MkDocs uses a standard folder structure to organize its configuration file and Markdown files.
The MkDocs "project" consists of the following:

* Folder where the MkDocs files reside.
* `mkdocs.yaml` configuration file listing the Markdown files that are a part of the website, and other configuration properties.
* `docs/` folder containing Markdown files, images, and other content.
* `site/` folder that will be generated containing the static website content.

The MkDocs documentation is straightforward and provides examples of the `mkdocs.yaml` configuration file.
See [Writing your docs](http://www.mkdocs.org/user-guide/writing-your-docs/).

## MkDocs Project in Git Repository

It is common that a MkDocs project would reside in a Git repository.
The repository may only contain documentation (similar to this documentation) or
the repository may, for example, contain software or other files and the MkDocs project is a secondary component.
The following sections provide recommendations for organizing files in the repository.
It is assumed that the repository folder already exists, for example due to cloning the repository from GitHub,
Bitbucket, or other cloud location.

### MkDocs Project is Only Repository Content

The repository for this documentation is named `owf-learn-mkdocs`.
When cloned from GitHub, a folder will be created with the same name.
Rather than assign unique names to each MkDocs project,
it is recommended to simply use `mkdocs-project` for the name, which will result in the following file structure:

```
owf-learn-mkdocs/                  (Git repository folder, under which resides .git, etc.)
  README.md
  .gitattributes
  .gitignore
  build-util/                      (see Deployment section of this documentation)
  mkdocs-project/                  (MkDocs project location, under which are all MkDocs files)
    .gitignore                     (Use a separate .gitignore file to ignore the dynamic site/ folder)
    mkdocs.yaml                    (MkDocs project configuration file)
    docs/                          (Folder where Markdown and other content files exist)
      *.md 
    site/                          (Folder automatically created by MkDocs software)
      index.html                   (Default landing page for static website)
```

The above convention ensures that whenever a `mkdocs-project` folder is found in a repository,
it should be obvious that a MkDocs project is present.

See [Create New MkDocs Project](#create-new-mkdocs-project) below for instructions on creating the above files.

### Mkdocs Project is a Component of Repository

A modification to the previous section can be used in cases where the MkDocs static website is a component of a repository.
Most software repositories will have a folder `src` for source code.
It is recommended to create one or more MkDocs project folders parallel to the `src` folder:

* `doc-dev-mkdocs-project` - for developer documentation
* `doc-user-mkdocs-project` - for user documentation

The files under the above folders should be similar to the previous section.

See [Create New MkDocs Project](#create-new-mkdocs-project) below for instructions on creating the above files.

## Create New MkDocs Project

There are two primary ways to start a new project, both of which will result in a file structure similar to that described in previous sections.

### Create MkDocs Project from Scratch

To create a MkDocs project from scratch, change to the repository folder and run the following command:

```sh
$ mkdocs new mkdocs-project
INFO    -  Creating project directory: mkdocs-project
INFO    -  Writing config file: mkdocs-project\mkdocs.yml
INFO    -  Writing initial docs: mkdocs-project\docs\index.md
```

This will create template `mkdocs.yaml` and `docs/index.html` files.
The files then need to be edited to configure website organization and content.

### Copy an Existing MkDocs Project's Files

Creating a MkDocs project from scratch as described in the previous section does not do much work.
Consequently, it may be easier to copy and modify an existing MkDocs project.
To do so, manually create the `mkdocs-project` folder under the repository folder and copy files from another MkDocs project,
in particular the `mkdocs.yaml` configuration file and git-related files (`.gitignore`, `.gitattributes`).
Manually create (or copy) the `docs/` folder and any files that should serve as the starting point for the new MkDocs project content.

Edit the files to configure the website organization and content.

## Git Repository Configuration Files

The following are examples of Git repository configuration files that should be included with the documentation files.
In the main Git folder include a `.gitignore` file to avoid committing temporary files from text editors:

```
# Ignore the following files (do not commit working files to repository)
# - see other .gitignore in mkdocs-project folder, to exclude auto-generated site

# Ignore temporary files from editors

*.swp
*.swo

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

In the main Git folder include a `.gitattributes` file to ensure that text files are saved with newline characters
and checked-out files use the operating system end of line:

```
# Settings for the repository

# Cause line endings in the repository to be newline (\n) and local files to be that of the operating system.
* text=auto

# Denote binary files

*.png binary
*.jpg binary
```

In the `mkdocs-project` folder, add an additional `.gitignore` file to ignore the dynamically-created `site/` folder:

```
# Ignore the following files (do not commit working files to repository)

# Ignore the site files since they are auto-generated and do not need to be under revision control.

site/

```

## Next Steps

Next, edit the website content.
