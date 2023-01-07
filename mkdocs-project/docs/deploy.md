# MkDocs / Deploy Website #

Running `mkdocs serve` to interactively edit and view the website does not generate the `site` folder
because the Python MkDocs application keeps the content in memory.
The `site/` folder in the MkDocs project is populated with the static website content by running `mkdocs build`.
Once the files are created, they can be deployed to a location where a web server can publish the files for viewing.

By convention, using a top-level page named `index.html` ensures that the site can be accessed using
either a URL to the `index.html` file, or the folder containing that file.

*   [Deploy to Amazon S3](#deploy-to-amazon-s3)
*   [Deploy Website to Google Cloud Platform](#deploy-website-to-google-cloud-platform)
*   [Deploy to WordPress](#deploy-to-wordpress)

------------------------

## Deploy to Amazon S3 ##

One way to serve the static website files is to copy the files to an
[Amazon S3 static website bucket](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)
or other static hosting solution.

The [`copy-to-owf-amazon-s3.sh`](https://github.com/OpenWaterFoundation/owf-learn-mkdocs/blob/master/build-util/copy-to-owf-amazon-s3.sh)
script illustrates how to copy the files to Amazon S3 using the Amazon command line interface tools,
in this case using a `sh` script designed to run on MinGW (Git Bash), Cygwin, and Linux.
The script expects to be provided with an Amazon web services profile name via script command parameter.
The script is in this case named `copy-to-owf-amazon-s3.sh` and is located in the `build-util` folder in the repository.

The `aws` command line script will have been installed using pip
(see [AWS CLI installation documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)).
To ensure that the package is installed with the same version of Python as `mkdocs`,
first list Python versions using `py --list`.
To control the `awscli` installation, use a command like `py -m pip install awscli`,
which will use the pip corresponding to latest Python.
Similar commands can be used to install for a specific version of Python,
for example `py -3.7 -m pip install awscli` or similar.
See also [OWF / Learn Amazon Web Services](http://learn.openwaterfoundation.org/owf-learn-aws/).

The `copy-to-owf-amazon-s3.sh` script does the following:

*   The `mkdocs build` command is run first to ensure that the `site` folder contains current website files.
*   The `site` folder is renamed to `owf-learn-mkdocs` during the upload to S3 bucket.
*   The default `index.html` file is used as the main page for the deployed site, as per normal website conventions.
    See the [deployed website](http://learn.openwaterfoundation.org/owf-learn-mkdocs/).

Using such a script allows the following:

*   run the script from any folder
*   check the version of MkDocs
*   automate processing, for example if part of a build process

## Deploy Website to Google Cloud Platform ##

A similar approach can be taken to deploy to Google Cloud Platform.
For example see the
[TSTool OpenCDSS](https://github.com/OpenCDSS/cdss-app-tstool-doc-user/blob/master/build-util/copy-to-co-dnr-gcp.sh)
script.

## Deploy to WordPress ##

A similar approach can be taken to deploy to WordPress website as static content (need to insert an example).
