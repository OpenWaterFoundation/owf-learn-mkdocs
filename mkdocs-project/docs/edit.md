# MkDocs / Edit Content #

Website content pages are created/edited with a text editor.
Each markdown file that is created should be included in the `mkdocs.yml` configuration file so that the MkDocs
software can process from Markdown into final form.
The remainder of this page contains the following sections:

*   [Markdown Introduction](#markdown-introduction)
*   [Markdown Text Editors](#markdown-text-editors)
*   [Selecting a Theme](#selecting-a-theme) - used to customize look and feel of MkDocs website
    +   [Custom CSS Configuration](#custom-css-configuration) - control HTML element formatting
* [Starting Local Web Server to Review Content](#starting-local-web-server-to-review-content) - shows website in browser
    +   [Stopping MkDocs Web Server](#stopping-mkdocs-web-server)
*   [Selecting File Naming Convention](#selecting-file-naming-convention) - conventions to organize files
*   [Selecting Markdown Documentation Styles](#selecting-markdown-documentation-styles) - conventions within the pages
*   [MkDocs Markdown Examples](#mkdocs-markdown-examples) - useful examples and tips
    +   [Image](#image):
        -   [Image - Center image and caption with link to full-size image](#image-center-image-and-caption-with-link-to-view-full-size-image)
    +   [Link](#link):
        -   [Link - Link to  a Markdown file in the same or different folder](#link-link-to-a-markdown-file-in-the-same-or-different-folder)
        -   [Link - Link to a heading in Markdown file](#link-link-to-a-heading-in-markdown-file)
        -   [Link - Link to a named location that is not a section heading](#link-link-to-a-named-location-that-is-not-a-section-heading)
    +   [List](#list):
        -   [List - Ensuring incremental numbers](#list-ensuring-incremental-numbers)
    +   [Table](#table):
        -   [Table - Controlling width of table columns](#table-controlling-width-of-table-columns) - helpful when defaults are not working well
        -   [Table - Center table and caption](#table-center-table-and-caption)
    +   [Text](#text):
        -   [Text - Format for readability and version control](#text-format-for-readability-and-version-control)
        -   [Text - Showing Markdown as literal text](#text-showing-markdown-as-literal-text) - used to show how to use Markdown
        -   [Text - Include language indicator for more specific formatting](#text-include-language-indicator-for-more-specific-formatting)

-----------------

## Markdown Introduction ##

The MkDocs documentation is straightforward and provides examples of content.
See the following MkDocs and Markdown resources to help with formatting content.
Additionally, because Markdown is text, one of the best ways to learn is to view the source files
for a Markdown document.
For example, [view the source files for this documentation on GitHub](https://github.com/OpenWaterFoundation/owf-learn-mkdocs).
Note that GitHub will render the Markdown in formatted form.  To view the source Markdown file,
click on the `.md` file of interest and use the ***Raw*** button.
The following are references for Markdown:

*   [Writing your docs](http://www.mkdocs.org/user-guide/writing-your-docs/)
*   [Mastering Markdown on GitHub](https://guides.github.com/features/mastering-markdown/)
*   [Adam Prichard's Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Markdown Text Editors ##

Editing Markdown requires a text editor.
Support for Markdown is being added to text editors over time,
typically by providing a text editing panel and a parallel view/render panel to show the formatted result.
These features are not needed with MkDocs because MkDocs formats Markdown as HTML for viewing
in a web browser.
However, a Markdown editor is still useful for README.md files that are used in the repository.

The following are text editors that provide Markdown viewing features:

*   [Visual Studio Code](https://code.visualstudio.com/) - use ***Ctrl-Shift-v*** to display the Markdown viewer
*   [Atom](https://atom.io/) - use ***Ctrl-Shift-m*** to display the Markdown viewer

## Selecting a Theme ##

The `mkdocs.yml` file allows a theme to be specified, which controls the look and feel of the website,
including menu features, whether search is enabled, and cascading style sheet (CSS) defaults for fonts, colors, etc.
For example, the following uses one of the default themes distributed with MkDocs
(see also the [Read the Docs website](https://readthedocs.org/), which is a public location for documents).

```yaml
theme:
  name: readthedocs
```

Changing the theme involves installing the theme files and changing the configuration file.

Experience has shown the following:

*   The default themes shipped with MkDocs (`readthedocs` and `mkdocs`) are generally adequate but have limitations,
    especially for larger sites.
    In particular, the navigation features are limited.
*   Sites having many documents can cause the left navigation bar to get very long, for example in `readthedocs` theme.
*   A menu-based theme with many menus at the top of the page can cause the page header to overflow and overwrite the top of pages.
    It is necessary in this case to limit the number of menus or words in menus in order to fit the maximum page width.
*   Some themes provide search features and some do not.  If a search feature is desirable then make sure to
    confirm that the theme includes this functionality.

Overcoming these issues requires experimenting with themes and perhaps adding custom CSS configuration.
It may also be desirable to customize the branding of documentation, which involves adding favicon and editing the CSS.

***Based on experimentation, the Material theme has been selected for this and other documentation.***
The Material theme provides search features, navigation for the entire site (left navigation panel),
navigation within a page (right navigation panel), and is also mobile-friendly
([responsive](https://en.wikipedia.org/wiki/Responsive_web_design)).
This documentation uses the Material theme.

To use a third-party theme, review the features of a theme and follow installation instructions.
[See the Install MkDocs section](install.md) for more information.

After installing the theme, change the `theme` configuration property in the `mkdocs.yml` file to indicate the new theme.
It may be necessary to and restart MkDocs (see next section).

### Custom CSS Configuration ###

Custom CSS configuration can be set to control the appearance of HTML elements.
If using the Material theme, the following is useful to add to the `mkdocs.yml` file to control CSS.

```
# Use extra CSS to customize styles, based on theme
extra_css:
  - 'css/extra-material-theme.css'
```

The following custom CSS configuration ensures that multiple levels of bulleted lists appear correctly
(default behavior is to use solid dots for all levels):

```
/* Custom styles to override MkDocs defaults and enhance theme */

/* Unordered list <ul> symbols:
 * - level 2 is hollow circle
 * - level 3 is filled square
 * - ul default is filled disc (bullet)
 */
article ul ul {
        list-style-type:  circle !important;
}

article ul ul ul {
        list-style-type:  square !important;
}

/*
 * Older Material theme used dark grey background with bold white text for table heading.
 * Newer Material uses white background with bold black text, but the heading does not stand out well.
 * Instead, set the background to a light gray, which works OK.
*/
thead th {
        background-color: #cccccc;
}
```

## Starting Local Web Server to Review Content ##

The MkDocs software converts the Markdown files into a static website that uses HTML, CSS, JavaScript, images, and other files.
The conversion of Markdown files to static website content takes place in two ways:

1.  In memory when a local MkDocs web server is run  with `mkdocs serve` (no output files are generated in the `site` folder).
2.  As files in the `site` folder when `mkdocs build` is run.

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

It is often helpful to use a script to run processes.
The [`run-mkdocs-serve-8000.sh`](https://github.com/OpenWaterFoundation/owf-learn-mkdocs/tree/master/build-util/run-mkdocs-serve-8000.sh)
script for MinGW (Git Bash), Cygwin,
and Linux illustrates how to run the MkDocs server on a port 8000 (the default) for this documentation.
A similar script can be used to run on a specific port,
which is useful when multiple servers need to be run at the same time.
The following can be dealt with in such a script:

*   Make sure that the script can be run from any folder and still work.
*   Find an appropriate Python to run `mkdocs` - can specify the `mkdocs` module to run,
    no need to run a script.
*   Confirm that the correct version of MkDocs is run for MkDocs files (e.g., require MkDocs 1+).
*   Potentially, make adjustments to the content programmatically.

### Stopping MkDocs Web Server ###

To stop the MkDocs web server, enter `Ctrl-C` in the command shell.  Only one MkDocs server can run at the same time for a port number.

## Selecting File Naming Convention ##

The Markdown files should follow a naming convention that facilitates maintaining the content,
for example:

*   Use consistent convention such as all lowercase with dashes separating words, for example `deploy-website` (folder)
    and `deploy-website.md` (Markdown file).
*   If images are used, create a folder such as `images` for imaged in a content folder.

It is possible that other documentation will link to a page so some care should be taken not to frequently change filenames.

## Selecting Markdown Documentation Styles ##

One of the benefits of using Markdown, MkDocs, and MkDocs theme is that styles are defaulted.
For example, using the `#` headings will result in a font style.
However, there is still a need to decide how Markdown will be applied to format a document.
It is possible to customize the MkDocs theme that is used to control such styles.
Another styling approach is to decide how to use basic Markdown to format documentation.
For example, the following may be selected as a convention for styling:

*   Indicate all user input with triple-backticks using appropriate content type.
*   Indicate all inline text program names with surrounding single-backticks.
*   Use italic bold (three surrounding asterisks) for software labels/features such as buttons to click.

Other choices can be made to ensure consistency in the documentation.

## MkDocs Markdown Examples ##

The following are useful examples and tips determined through use of MkDocs.
The content is grouped according to the element type.

### Image ###

#### Image - Center image and caption with link to view full-size image ####

MkDocs by default left-justifies images and text.
MkDocs also sizes images to fit within the width of the formatted page.
This can lead to ugly alignment and images being too small to clearly read.
The following can be inserted in the Markdown file to center the image and
its caption and provide a link to the full-size image.
In this example the image file is in a folder named `images.`

**<p style="text-align: center;">
![OWF-Logo-Color.png](images/OWF-Logo-Color.png)
</p>**

**<p style="text-align: center;">
Example Image (<a href="../images/OWF-Logo-Color.png">see full-size image</a>)
</p>**

```
**<p style="text-align: center;">
![OWF-Logo-Color.png](images/OWF-Logo-Color.png)
</p>**

**<p style="text-align: center;">
Example Image (<a href="../images/OWF-Logo-Color.png">see full-size image</a>)
</p>**
```

Technical notes:

*   It is also possible to add custom CSS to handle formatting,
    but care must be taken to not interfere with other CSS properties.
*   The `**` around the image is necessary and if removed will result in no image.
    Such formatting tricks may need to be evaluated for specific themes.
*   `../` must be used when linking to the full-size image, necessary due to how the final HTML is constructed.

### Link ###

#### Link - Link to a Markdown file in the same or different folder ####

A Markdown file can be linked to in the same folder by using the link notation.
The name of the markdown file with `.md` is specified in parentheses.
MkDocs prior to version 1 (?) allowed omitting the file extension but this seems to break links in version 1.0 and later,
where the MkDocs
[`use_directory_urls: true` configuration property](https://www.mkdocs.org/user-guide/configuration/#use_directory_urls)
is the default in MkDocs as of version 1.

```text
[text for visible link](other-markdown-file.md)
```

If the file exists in a different folder, specify a leading path:

```text
[text for visible link](../some-folder/other-markdown-file.md)
```

#### Link - Link to a heading in Markdown file ####

Use the following syntax to link to a heading in a separate file, where the words in parenthesis match the
`#` heading.  This is useful for creating internal table of contents to help with navigation.
The following are rules for specifying the reference location in parentheses:

*   Start the location name with a `#`.
*   Replace spaces by dash.
*   Remove periods and some other special characters as necessary to make the link work.
*   Use all lowercase in the location name.

```text
[text for visible link](../parallel-folder/other-markdown-file.md#heading-words)

```

If the link is to a location in the current file, omit the leading filename and start the reference with `#`.

#### Link - Link to a named location that is not a section heading ####

It can be useful to include a link to a point within a Markdown file without referring to a heading.
To do so, add the following to create a named location:

```text
1. <a name="step1"></a>Some text for step 1 in a process.
```

Then add a link to the named location similar to the following:

```text
Press "back" in the browser to return to the list of setup steps or [click here](#step1)`
```

### List ###

#### List - Ensuring incremental numbers ####

Complicated lists may result in numbers resetting rather than continuing in a sequence.
This can be particularly challenging when list levels include images and code blocks.
Markdown does not require the numbers in a list to be sequential,
which is helpful when lists are long and it is a chore to renumber based on a change.
However, this lazy approach can result in problems.
The following are suggestions that may help.

##### Make sure to indent intervening content #####

A list with intervening content at a lesser indent rests numbering.
For example:

---

Markdown:

```
1.  Item 1.
2.  Item 2.

Some text

3.  Item 3.
```

Result (note reset in numbers):

1.  Item 1.
2.  Item 2.

Some text

3.  Item 3.

---

Markdown:

```
1.  Item 1.
2.  Item 2.

    Some text

3.  Item 3.
```

Result (note sequential numbers):

1.  Item 1.
2.  Item 2.

    Some text

3.  Item 3.

---

The following shows an image.

---

Markdown:

```
1.  Item 1.
2.  Item 2.

![image](images/OWF-Logo-Color.png)

3.  Item 3.
```

Result (note reset in numbers):

1.  Item 1.
2.  Item 2.

![image](images/OWF-Logo-Color.png)

3.  Item 3.

---

Markdown:

```
1.  Item 1.
2.  Item 2.

    ![image](images/OWF-Logo-Color.png)

3.  Item 3.
```

Result (note sequential numbers):

1.  Item 1.
2.  Item 2.

    ![image](images/OWF-Logo-Color.png)

3.  Item 3.

---

### Table ###

#### Table - Controlling width of table columns ####

Markdown tables in MkDocs sites set table column widths based on the amount of content in each column.
Wider columns are used for columns with more characters/words.
This can lead to undesirable results, such as line breaks in the middle of words.
It is possible to insert HTML characters such as the non-breaking-hyphen (`&#8209;`);
however, this leads to ugly content and it may not be possible to control all breaks.

Another option is to include the non-breaking space characters in the header of the table sufficient to make the column wide enough, for example:

| **Parameter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;** | **Description** | Default |
| -------- | --------- | --------- |
| `--some-option` | This is a command parameter | default value | 

Source:

```
| **Parameter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;** | **Description** | Default |
| -------- | --------- | --------- |
| `--some-option` | This is a command parameter | default value | 
```

#### Table - Center table and caption ####

A simple table is as follows:

| **Parameter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;** | **Description** | Default |
| -------- | --------- | --------- |
| `--some-option` | This is a command parameter | default value | 

To center the table and its caption:

**Unfortunately, don't have centering a table figured out yet - this may be difficult due to CSS handling of sizing and scrolling.**

<div style="text-align: center;">
| **Parameter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;** | **Description** | Default |
| -------- | --------- | --------- |
| `--some-option` | This is a command parameter | default value | 
</div>

**<p style="text-align: center;">
Table Caption
</p>**

### Text ###

#### Text - Format for readability and version control ####

Markdown has minimal restrictions on text formatting.
For example, a paragraph's text can be split across lines or one lone line.
However, formatting text with some care will result in greater readability and
easier use with version control, as described below.

##### Indent each line of list content #####

Lists use 4 spaces for indentation. 
The following formatting will work:

```
1. First item, first line
Second line
2. Second item, first line
Second line
```

1. First item, first line
Second line
2. Second item, first line
Second line

However, the above is more difficult to read if the source file is edited with a text editor.
The following formatting is easier to read and helps organize complicated content.
Note that the 4-space indentation accommodates up to 99 levels.

```
1.  First item, first line
    Second line
2.  Second item, first line
    Second line
```

##### Use line breaks to improve granularity of version control #####

If Markdown paragraph text is formatted without line breaks,
then a change of one character anywhere in the long line will be tracked in a version control system.
Doing a "diff" on the files will show that there is a change in the paragraph.
However, if line breaks are used, the difference can be more easily shown
to within a sentence or sub-sentence, which improves the granularity of version control.
A general rule is to keep lines similar to software code, such as 80-120 characters maximum.
For example, break lines at punctuation, Markdown elements such as links, etc.

#### Text - Showing Markdown as literal text ####

It is often useful to show examples of Markdown, such as in this documentation.
To do so, indent the Markdown by 4 spaces, as shown in the following example.
The back ticks will be shown as typed in the source file and are not interpreted as formatting.

    ```sh
    $ some-shell-command
    ```

Alternatively, without the leading spaces the above is rendered as follows:

```sh
$ some-shell-command
```

#### Text - Include language indicator for more specific formatting ####

It is useful to automatically format content based on the language for the content.
For example, the following uses notation <code>```sh</code> to indicate that the content is for a Linux shell script:

```sh
# Some script
cd someDir
ls -la
```
Source Markdown:

    ```sh
    # Some script
    cd someDir
    ls -la
    ```


The following provides a list of languages supported by Markdown, although support will vary by tool:

*   [GitHub Markdown language file](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)
*   [Languages Supported by Github Flavored Markdown](http://www.rubycoloredglasses.com/2013/04/languages-supported-by-github-flavored-markdown/)
