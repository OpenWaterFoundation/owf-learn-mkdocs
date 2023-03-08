#!/bin/sh
(set -o igncr) 2>/dev/null && set -o igncr; # This comment is required.
# The above line ensures that the script can be run on Cygwin/Linux even with Windows CRNL.
#
# Run 'mkdocs serve' on port 8000 (default) for MkDocs 1.x.
#
# The most recent version of this script is saved with Open Water Foundation owf-learn-mkdocs GitHub repository.
# If changes are implemented, the version in owf-learn-mkdocs/build-util should be updated as the global master.
# If necessary, run 'dos2unix' or 'unix2dos' (or equivalent) to ensure that line endings are OK in the copied script.
#
# -------------------------------------------------------------------------------------------------------------
# This script attempts to find a suitable Python and mkdocs module for cygwin, Git bash, and Linux.
# The script is assumed to be installed in one of two configurations, for example:
#
# Option 1 - repository is dedicated to the documentation:
#
# main-repo-folder/
#   mkdocs-project/
#     mkdocs.yml
#   build-util/
#     this-script
#   doc/
#   site/
#
# Option 2 - repository contains more than the documentation and documentation is in a top-level folder,
# for example:
#
# main-repo-folder/
#   doc-dev-mkdocs-project/
#     mkdocs.yml
#     build-util/
#       this-script
#     doc/
#     site/
#
# In either case, a standard MkDocs folder structure is assumed with 'mkdocs.yml' configuration file,
# 'docs/' folder for source files, and 'site/' folder for MkDocs-generated static website.
# -------------------------------------------------------------------------------------------------------------

# Supporting functions, alphabetized.

# Check the folder depth for the MkDocs project:
# - the folder where this script lives may be at various levels relative to the main MkDocs project folder
# - depends on "scriptFolder" having been set
checkFolderDepth() {
  folderDepth=999
  if [ -e "${scriptFolder}/../mkdocs-project/mkdocs.yml" ]; then
    folderDepth=1
  elif [ -e "${scriptFolder}/../../mkdocs-project/mkdocs.yml" ]; then
    folderDepth=2
  fi
}

# Make sure the MkDocs version is consistent with the documentation content:
# - require that at least version 1.0 is used because of use_directory_urls = True default
# - must use "file.md" in internal links whereas previously "file" would work
# - it is not totally clear whether version 1 is needed but try this out to see if it helps avoid broken links
checkMkdocsVersion() {
  # Required MkDocs version is at least 1.
  requiredMajorVersion="1"
  # On Cygwin, mkdocs --version gives:  mkdocs, version 1.0.4 from /usr/lib/python3.6/site-packages/mkdocs (Python 3.6)
  # On Debian Linux, similar to Cygwin:  mkdocs, version 0.17.3
  # On newer windows: MkDocs --version:  python -m mkdocs, version 1.3.1 from C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\mkdocs (Python 3.10)
  # The following should work for any version after a comma.
  mkdocsVersionFull=$(${mkdocsExe} --version | sed -e 's/.*, \(version .*\)/\1/g' | cut -d ' ' -f 2)
  echo "MkDocs --version:  ${mkdocsVersionFull}"
  mkdocsVersion=$(echo "${mkdocsVersionFull}" | cut -d ' ' -f 3)
  if [ -z "${mkdocsVersion}" ]; then
    echo "Error getting MkDocs version.  Is it installed?"
    exit 1
  fi
  echo "MkDocs full version number:  ${mkdocsVersion}"
  mkdocsMajorVersion=$(echo "${mkdocsVersion}" | cut -d '.' -f 1)
  echo "MkDocs major version number:  ${mkdocsMajorVersion}"
  if [ "${mkdocsMajorVersion}" -lt "${requiredMajorVersion}" ]; then
    echo ""
    echo "MkDocs version for this documentation must be version ${requiredMajorVersion} or later."
    echo "MkDocs version that is found is ${mkdocsMajorVersion}, from full version ${mkdocsVersion}."
    exit 1
  else
    echo ""
    echo "MkDocs major version (${mkdocsMajorVersion}) is OK for this documentation."
  fi
}

# Determine the operating system that is running the script
# - mainly care whether Cygwin or MINGW
checkOperatingSystem() {
  if [ ! -z "${operatingSystem}" ]; then
    # Have already checked operating system so return
    return
  fi
  operatingSystem="unknown"
  os=`uname | tr [a-z] [A-Z]`
  case "${os}" in
    CYGWIN*)
      operatingSystem="cygwin"
      ;;
    LINUX*)
      operatingSystem="linux"
      ;;
    MINGW*)
      operatingSystem="mingw"
      ;;
  esac
  echo "Detected operating system:  ${operatingSystem}"
}

# Check the source files for issues:
# - the main issue is internal links need to use [](file.md), not [](file)
checkSourceDocs() {
  # Currently don't do anything but could check the above
  # Need one line to not cause an error
  :
}

# Set the MkDocs executable to use, depending operating system and PATH:
# - sets the global ${mkdocsExe} variable
# - return 0 if the executable is found, exit with 1 if not
setMkDocsExe() {
  if [ "${operatingSystem}" = "cygwin" ] || [ "${operatingSystem}" = "linux" ]; then
    # Is usually in the PATH.
    mkdocsExe="mkdocs"

    mkdocs --version

    # Check if the last command worked, and if not, try `py -m mkdocs --version`.
    if [ "$?" = "1" ]; then
      mkdocsExe="py -m mkdocs"
      return 0
    fi

    if hash py 2>/dev/null; then
      echo "mkdocs is not found (not in PATH)."
      exit 1
    fi
  elif [ "${operatingSystem}" = "mingw" ]; then
    # This is used by Git Bash:
    # - calling 'hash' is a way to determine if the executable is in the path
    if hash py 2>/dev/null; then
      mkdocsExe="py -m mkdocs"
    else
      # Try adding the Windows folder to the PATH and rerun:
      # - not sure why C:\Windows is not in the path in the first place
      PATH=/C/Windows:${PATH}
      if hash py 2>/dev/null; then
        mkdocsExe="py -m mkdocs"
      else
        echo 'mkdocs is not found in C:\Windows.'
        exit 1
      fi
    fi
  fi
  return 0
}

# Entry point into the script.

# Get the folder where this script is located since it may have been run from any folder.
scriptFolder=$(cd $(dirname "$0") && pwd)

# Change to the folder where the script is since other actions below are relative to that.
cd ${scriptFolder}

# Check the operating system.
checkOperatingSystem

# Set the MkDocs executable:
# - will exit if MkDocs is not found
setMkDocsExe

# Make sure the MkDocs version is OK.
checkMkdocsVersion

# Check the source files for issues.
checkSourceDocs

# Determine if this script is one or two folders under MkDocs project folder.
checkFolderDepth

# Change to the folder where the script is since other actions below are relative to that.
cd "${scriptFolder}" || exit

# Change to the MkDocs project folder so that 'mkdocs' can be run and find files it expects.
cd ../mkdocs-project || exit

# Run the MkDocs server.
port=8000
echo "View the website using http://localhost:${port}"
echo "Stop the server with CTRL-C"
${mkdocsExe} serve -a 0.0.0.0:${port}

exit $?
