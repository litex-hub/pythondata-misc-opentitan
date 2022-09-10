import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14107"
version_tuple = (0, 0, 14107)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14107")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13965"
data_version_tuple = (0, 0, 13965)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13965")
except ImportError:
    pass
data_git_hash = "7e3bb0a70951a7542f13f7d7143c3f55acb0e8a1"
data_git_describe = "v0.0-13965-g7e3bb0a709"
data_git_msg = """\
commit 7e3bb0a70951a7542f13f7d7143c3f55acb0e8a1
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Mon Sep 5 14:38:50 2022 -0700

    [sw] Allow for the optional inclusion of a .bazelrc-site file
    
    The .bazelrc-site file allows for site-specific compile options
    (output roots, library paths etc).   This file is an optional
    addition to each working repository, however this file should
    not be added to the upstrem repository. Therefore this file
    is also added to .gitignore, and a CI check is added to
    entsure that this file is not forcibly added to git where
    it could contaminate the site-specific setup of other users.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
