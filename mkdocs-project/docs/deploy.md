# Learn MkDocs / Deploy Website

The `site/` folder in the MkDocs project will be populated with static website content by running `mkdocs build`.
Once the files are created, they can be deployed to a location where a web server can publish the files.

## Deploy to Amazon S3

One way to serve the static website files is to copy the files to an
[Amazon S3 static website bucket](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).

The following script illustrates how to copy the files to Amazon S3 using the Amazon command line interface tools,
in this case using a `Linux` bash script, and a provided Amazon web services profile via script command parameter.
The script is in this case named copyToOwfAmazonS3.sh and is located in the `build-util` folder in the repository.


```
#!/bin/bash
#
# Copy the site/* contents to the learn.openwaterfoundation.org website
# - replace all the files on the web with local files
# - location is learn.openwaterfoundation.org/owf-learn-mkdocs
# - must specify Amazon profile

# Set --dryrun to test before actually doing
dryrun=""
#dryrun="--dryrun"
s3Folder="s3://learn.openwaterfoundation.org/owf-learn-mkdocs"

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
