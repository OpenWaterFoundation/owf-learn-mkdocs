# Learn MkDocs / New MkDocs Project #

MkDocs uses a standard folder structure to organize its configuration file and Markdown content files.
The MkDocs "project" (for example a folder named `mkdocs_project`) consists of the following:

* `mkdocs.yml` configuration file listing the Markdown files that are a part of the website, and other configuration properties.
	+ For example, see the [repository `mkdocs.yml`](https://github.com/OpenWaterFoundation/owf-learn-mkdocs/blob/master/mkdocs-project/mkdocs.yml)
	file for this documentation.
	+ Markdown files must be listed in this file in order to be processed into website HTML content.
* `docs/` folder containing Markdown files, images, and other content.
	+ Folders can be used for content sections
	+ Folder can be used for linked files such as images and examples.
* `site/` folder that will be generated containing the static website content.
	+ Contents can be copied to a cloud location to publish the website.

The MkDocs documentation is straightforward and provides examples of the `mkdocs.yml` configuration file.
See [Writing your docs in the MkDocs documentation](http://www.mkdocs.org/user-guide/writing-your-docs/).

This page contains the following sections:

* [MkDocs Project Conventions for Git Repository](#mkdocs-project-conventions-for-git-repository)
	+ [MkDocs Project is Only Repository Content](#mkdocs-project-is-only-repository-content) - repository is dedicated to documentation
	+ [MkDocs Project is a Component of Repository](#mkdocs-project-is-a-component-of-repository) - for example, documentation for software product
* [Create New MkDocs Project](#create-new-mkdocs-project)
	+ [Create MkDocs Project from Scratch](#create-mkdocs-project-from-scratch)
	+ [Copy an Existing MkDocs Project's Files](#copy-an-existing-mkdocs-projects-files) - useful if new documentation is similar to other documentation
* [Git Repository Configuration Files](#git-repository-configuration-files)
* [Next Steps](#next-steps)

## MkDocs Project Conventions for Git Repository ##

It is common that a MkDocs project will reside in a Git repository in order to track versions of file content.
The repository may only contain documentation (similar to this documentation) or
the repository may, for example, contain software or other files and the MkDocs project is a secondary component.
The following sections provide recommendations for organizing files in the repository.
It is assumed that the repository folder already exists, for example due to cloning the repository from GitHub,
Bitbucket, or other cloud location.

### MkDocs Project is Only Repository Content ###

The repository for this documentation is named `owf-learn-mkdocs`.
When cloned from GitHub, a folder will be created with the same name.
Rather than assign unique names to each MkDocs project,
it is recommended to simply use `mkdocs-project` for the name, which will result in the following file structure:

```text
owf-learn-mkdocs/                  (Git repository folder, under which resides .git, etc.)
  README.md                        (As per GitHub, etc. conventions)
  .gitattributes                   (As per Git conventions)
  .gitignore
  build-util/                      (See Deployment section of this documentation)
  mkdocs-project/                  (MkDocs project location, under which are all MkDocs files)
    .gitignore                     (Can use a separate .gitignore file to ignore the dynamic site/ folder)
    mkdocs.yml                     (MkDocs project configuration file)
    docs/                          (Folder where Markdown and other content files exist)
      *.md 
    site/                          (Folder automatically created by MkDocs software)
      index.html                   (Default landing page for static website)
      many other files
```

The above convention ensures that whenever a `mkdocs-project` folder is found in a repository,
it should be obvious that a MkDocs project is present.
Every file under the folder will adhere to MkDocs conventions and other files can be added outside of these files,
for example to upload the website to a cloud location.

See [Create New MkDocs Project](#create-new-mkdocs-project) below for instructions on creating the above files.

### MkDocs Project is a Component of Repository ###

A modification to the recommendations in the previous section can be used in cases
when the MkDocs static website is a component of a repository.
Most software repositories will have a folder `src` for source code.
It is recommended to create one or more MkDocs project folders parallel to the `src` folder, for example:

* `doc-dev-mkdocs-project` - for developer documentation
* `doc-user-mkdocs-project` - for user documentation

The files under the above folders should be similar to the previous section, for example where `mkdocs-project` (previous section) is
equivalent to `doc-dev-mkdocs-project` (below):

```text
some-git-repo-folder/                (Git repository folder, under which resides .git, etc.)
  README.md                          (As per GitHub, etc. conventions)
  .gitattributes                     (As per Git conventions)
  .gitignore
  doc-dev-mkdocs-project/            (Folder dedicated to a MkDocs project for developer documentation)
    build-util/                      (See Deployment section of this documentation)
    mkdocs-project/                  (MkDocs project location, under which are all MkDocs files)
      .gitignore                     (Can use a separate .gitignore file to ignore the dynamic site/ folder)
      mkdocs.yml                     (MkDocs project configuration file)
      docs/                          (Folder where Markdown and other content files exist)
        *.md 
      site/                          (Folder automatically created by MkDocs software)
        index.html                   (Default landing page for static website)
        many other files
  src/                               (Source code files in software project)
```

See [Create New MkDocs Project](#create-new-mkdocs-project) below for instructions on creating the above files.

## Create New MkDocs Project ##

There are two primary ways to start a new project, both of which will result in a file structure similar to that described in previous sections.

### Create MkDocs Project from Scratch ###

To create a MkDocs project from scratch, change to the repository folder and run the following command from a command shell:

```sh
$ mkdocs new mkdocs-project
INFO    -  Creating project directory: mkdocs-project
INFO    -  Writing config file: mkdocs-project\mkdocs.yml
INFO    -  Writing initial docs: mkdocs-project\docs\index.md
```

This will create template `mkdocs.yml` and `docs/index.html` files.
The files then need to be edited to configure website organization and content.

### Copy an Existing MkDocs Project's Files ###

Creating a MkDocs project from scratch as described in the previous section does not do much work.
Consequently, it may be easier to copy and modify an existing MkDocs project.
To do so, manually create the `mkdocs-project` folder under the repository folder and copy files from another MkDocs project,
in particular the `mkdocs.yml` configuration file and git-related files (`.gitignore`, `.gitattributes`).
Manually create (or copy) the `docs/` folder and any files that should serve as the starting point for the new MkDocs project content.

Edit the files to configure the website organization and content.
Make sure to clean up files before committing to the repository to avoid confusion with irrelevant files.

## Git Repository Configuration Files ##

The following are examples of Git repository configuration files that should be included with the documentation files.
In the main Git folder, include a `.gitignore` file to avoid committing temporary files from text editors:

```text
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

In the main Git folder, include a `.gitattributes` file to ensure that text files are saved with newline characters
and checked-out files use the operating system end of line:

```text
# Settings for the repository

# Cause line endings in the repository to be newline (\n) and local files to be that of the operating system.
* text=auto

# Denote binary files

*.png binary
*.jpg binary
```

In the `mkdocs-project` folder, add an additional `.gitignore` file to ignore the dynamically-created `site/` folder:

```text
# Ignore the following files (do not commit working files to repository)

# Ignore the site files since they are auto-generated and do not need to be under revision control.

site/

```

## Next Steps ##

Next, edit the website content.
