#! /usr/bin/env python
#
# THIS IS A HACK TO FIX BUG IN THE MkDocs gh-deploy command, which has some Unicode problem
# HARD CODE THE CALL TO ghp_import BECAUSE CALL FROM MkDocs gh_deploy COMMAND HAS EXCEPTION BELOW.
# SEE ALSO: https://github.com/mkdocs/mkdocs/issues/722
#
# SEE MAIN PROGRAM BELOW FOR USAGE.
#
#sam (master) mkdocs-project $ mkdocs gh-deploy --clean
#INFO    -  Cleaning site directory
#INFO    -  Building documentation to directory: C:\owf-gitrepos\owf-learn-cdss-statemod-dev\mkdocs-project\site
#INFO    -  Copying 'C:\owf-gitrepos\owf-learn-cdss-statemod-dev\mkdocs-project\site' to 'gh-pages' branch and pushing to GitHub.
#Traceback (most recent call last):
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\runpy.py", line 170, in _run_module_as_main
#    "__main__", mod_spec)
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\runpy.py", line 85, in _run_code
#    exec(code, run_globals)
#  File "C:\Users\sam\AppData\Local\Programs\Python\Python35-32\Scripts\mkdocs.exe\__main__.py", line 9, in <module>
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages\click\core.py", line 716, in __call__
#    return self.main(*args, **kwargs)
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages\click\core.py", line 696, in main
#    rv = self.invoke(ctx)
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages\click\core.py", line 1060, in invoke
#    return _process_result(sub_ctx.command.invoke(sub_ctx))
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages\click\core.py", line 889, in invoke
#    return ctx.invoke(self.callback, **ctx.params)
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages\click\core.py", line 534, in invoke
#    return callback(*args, **kwargs)
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages\mkdocs\__main__.py", line 189, in gh_deploy_command
#    gh_deploy.gh_deploy(config, message=message)
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages\mkdocs\commands\gh_deploy.py", line 69, in gh_deploy
#    remote_branch)
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages\mkdocs\utils\ghp_import.py", line 163, in ghp_import
#    if not try_rebase(remote, branch):
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages\mkdocs\utils\ghp_import.py", line 78, in try_rebase
#    if sp.call(cmd) != 0:
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\subprocess.py", line 560, in call
#    with Popen(*popenargs, **kwargs) as p:
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\subprocess.py", line 950, in __init__
#    restore_signals, start_new_session)
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\subprocess.py", line 1194, in _execute_child
#    args = list2cmdline(args)
#  File "c:\users\sam\appdata\local\programs\python\python35-32\lib\subprocess.py", line 754, in list2cmdline
#    needquote = (" " in arg) or ("\t" in arg) or not arg
#TypeError: a bytes-like object is required, not 'str'
#
# This file is part of the ghp-import package released under
# the Tumbolia Public License.

#                            Tumbolia Public License

# Copyright 2013, Paul Davis <paul.joseph.davis@gmail.com>

# Copying and distribution of this file, with or without modification, are
# permitted in any medium without royalty provided the copyright notice and this
# notice are preserved.

# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

#   0. opan saurce LOL

from __future__ import unicode_literals

import errno
import logging
import os
import subprocess as sp
import sys
import time
import unicodedata

log = logging.getLogger(__name__)


if sys.version_info[0] == 3:
    def enc(text):
        if isinstance(text, bytes):
            return text
        return text.encode()

    def dec(text):
        if isinstance(text, bytes):
            return text.decode('utf-8')
        return text

    def write(pipe, data):
        try:
            pipe.stdin.write(data)
        except IOError as e:
            if e.errno != errno.EPIPE:
                raise
else:
    def enc(text):
        if isinstance(text, unicode):
            return text.encode('utf-8')
        return text

    def dec(text):
        if isinstance(text, unicode):
            return text
        return text.decode('utf-8')

    def write(pipe, data):
        pipe.stdin.write(data)


def normalize_path(path):
    # Fix unicode pathnames on OS X
    # See: http://stackoverflow.com/a/5582439/44289
    if sys.platform == "darwin":
        return unicodedata.normalize("NFKC", dec(path))
    return path


def try_rebase(remote, branch):
    cmd = ['git', 'rev-list', '--max-count=1', '%s/%s' % (remote, branch)]
    p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
    (rev, _) = p.communicate()
    if p.wait() != 0:
        return True
    cmd = ['git', 'update-ref', 'refs/heads/%s' % branch, dec(rev.strip())]
    if sp.call(cmd) != 0:
        return False
    return True


def get_config(key):
    p = sp.Popen(['git', 'config', key], stdin=sp.PIPE, stdout=sp.PIPE)
    (value, _) = p.communicate()
    return value.decode('utf-8').strip()


def get_prev_commit(branch):
    cmd = ['git', 'rev-list', '--max-count=1', branch, '--']
    p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
    (rev, _) = p.communicate()
    if p.wait() != 0:
        return None
    return rev.decode('utf-8').strip()


def mk_when(timestamp=None):
    if timestamp is None:
        timestamp = int(time.time())
    currtz = "%+05d" % (-1 * time.timezone / 36)  # / 3600 * 100
    return "%s %s" % (timestamp, currtz)


def start_commit(pipe, branch, message):
    uname = dec(get_config("user.name"))
    email = dec(get_config("user.email"))
    write(pipe, enc('commit refs/heads/%s\n' % branch))
    write(pipe, enc('committer %s <%s> %s\n' % (uname, email, mk_when())))
    write(pipe, enc('data %d\n%s\n' % (len(message), message)))
    head = get_prev_commit(branch)
    if head:
        write(pipe, enc('from %s\n' % head))
    write(pipe, enc('deleteall\n'))


def add_file(pipe, srcpath, tgtpath):
    with open(srcpath, "rb") as handle:
        if os.access(srcpath, os.X_OK):
            write(pipe, enc('M 100755 inline %s\n' % tgtpath))
        else:
            write(pipe, enc('M 100644 inline %s\n' % tgtpath))
        data = handle.read()
        write(pipe, enc('data %d\n' % len(data)))
        write(pipe, enc(data))
        write(pipe, enc('\n'))


def add_nojekyll(pipe):
    write(pipe, enc('M 100644 inline .nojekyll\n'))
    write(pipe, enc('data 0\n'))
    write(pipe, enc('\n'))


def gitpath(fname):
    norm = os.path.normpath(fname)
    return "/".join(norm.split(os.path.sep))


def run_import(srcdir, branch, message, nojekyll):
    cmd = ['git', 'fast-import', '--date-format=raw', '--quiet']
    kwargs = {"stdin": sp.PIPE}
    if sys.version_info >= (3, 2, 0):
        kwargs["universal_newlines"] = False
    pipe = sp.Popen(cmd, **kwargs)
    start_commit(pipe, branch, message)
    for path, _, fnames in os.walk(srcdir):
        for fn in fnames:
            fpath = os.path.join(path, fn)
            fpath = normalize_path(fpath)
            gpath = gitpath(os.path.relpath(fpath, start=srcdir))
            add_file(pipe, fpath, gpath)
    if nojekyll:
        add_nojekyll(pipe)
    write(pipe, enc('\n'))
    pipe.stdin.close()
    if pipe.wait() != 0:
        sys.stdout.write(enc("Failed to process commit.\n"))


def ghp_import(directory, message, remote='origin', branch='gh-pages', force=False):

    if not try_rebase(remote, branch):
        log.error("Failed to rebase %s branch.", branch)

    nojekyll = True

    run_import(directory, branch, message, nojekyll)

    cmd = ['git', 'push', remote, branch]

    if force:
        cmd.insert(2, '--force')

    proc = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)

    out, err = proc.communicate()
    result = proc.wait() == 0

    return result, dec(err)

if [ __name__ == "__main__" ]:
    # Process the first argument as the directory
    if ( len(sys.argv) == 1 ):
        # Only program name so print usage
        print("")
        print("Usage:  python ghp_import.py folderName")
        print("")
        print("where folderName is the folder to use as the gh_pages branch in GitHub")
        print("")
    else:
        ghp_import(sys.argv[1], "Commit " + sys.argv[1] + " as GitHub Pages branch gh-pages", remote='origin', branch='gh-pages', force=False)

