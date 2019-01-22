# MkDocs / Deploy Website #

Running `mkdocs serve` to interactively edit and view the website does not generate the `site` folder
because the Python MkDocs application keeps the content in memory.
The `site/` folder in the MkDocs project is populated with the static website content by running `mkdocs build`.
Once the files are created, they can be deployed to a location where a web server can publish the files for viewing.

By convention, using a top-level page named `index.html` ensures that the site can be accessed using
either a URL to the `index.html` file, or the folder containing that file.

* [Deploy to Amazon S3](#deploy-to-amazon-s3)
* [Deploy Website to Google Cloud Platform](#deploy-website-to-google-cloud-platform)
* [Deploy to WordPress](#deploy-to-wordpress)

------------------------

## Deploy to Amazon S3 ##

One way to serve the static website files is to copy the files to an
[Amazon S3 static website bucket](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)
or other static hosting solution.

The [`copy-to-owf-amazon-s3.sh`](https://github.com/OpenWaterFoundation/owf-learn-mkdocs/blob/master/build-util/copy-to-owf-amazon-s3.sh)
script illustrates how to copy the files to Amazon S3 using the Amazon command line interface tools,
in this case using a Cygwin/Linux `sh` script that expects to be provided with an Amazon web services profile name via script command parameter.
The script is in this case named `copy-to-owf-amazon-s3.sh` and is located in the `build-util` folder in the repository.

The `mkdocs build` command is run first to ensure that the `site` folder contains current website files.
The `site` folder is renamed to `owf-learn-mkdocs` during the upload.
The default `index.html` file is used as the main page for the deployed site, as per normal website conventions.
See the [deployed website](http://learn.openwaterfoundation.org/owf-learn-mkdocs/).

Using such a script allows the following:

* run the script from any folder
* check the version of MkDocs
* specify the port number, in case multiple MkDocs servers are run at the same time
* automate modifying content, for example to support "latest" and versioned documentation, with links that
cross-link to other versioned documentation (this needs to be evaluated)

## Deploy Website to Google Cloud Platform ##

A similar approach can be taken to deploy to Google Cloud Platform (need to insert an example).

## Deploy to WordPress ##

A similar approach can be taken to deploy to WordPress website as static content (need to insert an example).
