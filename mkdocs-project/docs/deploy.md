# Learn MkDocs / Deploy Website

Running `mkdocs serve` to interactively edit and view the website does not generate the `site` folder
because the Python MkDocs application keeps the content in memory.
The `site/` folder in the MkDocs project is populated with the static website content by running `mkdocs build`.
Once the files are created, they can be deployed to a location where a web server can publish the files for viewing.

By convention, using a top-level page named `index.html` ensures that the site can be accessed using
either a URL to the `index.html` file, or the folder containing that file.

## Deploy to Web Server ##

If an organization runs their own web server or has access to a web server, the contents of the `site` file can be
copied to that web server and accessed in normal fashion by specifying a URL to the content.

## Deploy to Amazon S3

One way to serve the static website files is to copy the files to an
[Amazon S3 static website bucket](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)
or other static hosting solution.

The following [`copy-to-owf-amazon-s3.sh`](https://github.com/OpenWaterFoundation/owf-learn-mkdocs/blob/master/build-util/copy-to-owf-amazon-s3.sh)
script illustrates how to copy the files to Amazon S3 using the Amazon command line interface tools,
in this case using a Linux `sh` script that expects to be provided with an Amazon web services profile name via script command parameter.
This script can can also be used in Cygwin.
The script is in this case named `copy-to-owf-amazon-s3.sh` and is located in the `build-util` folder in the repository.
The `mkdocs build` command is run first to ensure that the `site` folder contains current website files.
The `site` folder is renamed to `owf-learn-mkdocs` during the upload.
The default `index.html` file is used as the main page for the deployed site, as per normal website conventions.


```sh
#!/bin/sh
#
# Copy the site/* contents to the learn.openwaterfoundation.org website
# - replace all the files on the web with local files
# - must specify Amazon profile

# Set --dryrun to test before actually doing
dryrun=""
#dryrun="--dryrun"
s3Folder="s3://learn.openwaterfoundation.org/owf-learn-mkdocs"

# Make sure that this is being run from the build-util folder
pwd=`pwd`
dirname=`basename ${pwd}`
if [ ! ${dirname} = "build-util" ]
        then
        echo "Must run from build-util folder"
        exit 1
fi

if [ "$1" == "" ]
        then
        echo ""
        echo "Usage:  $0 AmazonConfigProfile"
        echo ""
        echo "Copy the site files to the Amazon S3 static website folder:  $s3Folder"
        echo ""
        exit 0
fi

awsProfile="$1"

# First build the site so that the "site" folder contains current content.
# - "mkdocs serve" does not do this

cd ../mkdocs-project; mkdocs build --clean; cd ../build-util

# Now sync the local files up to Amazon S3
aws s3 sync ../mkdocs-project/site ${s3Folder} ${dryrun} --delete --profile "$awsProfile"
```

## Deploy Website to Google Pages

**TODO smalers 2016-11-27 Need to document, but had some issues due to MkDocs bug - seems to be fixed with MkDocs 0.16.0?**
