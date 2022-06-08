import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12572"
version_tuple = (0, 0, 12572)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12572")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12430"
data_version_tuple = (0, 0, 12430)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12430")
except ImportError:
    pass
data_git_hash = "13babd7d1d9ebea34e97b15277ffb1be794ab376"
data_git_describe = "v0.0-12430-g13babd7d1"
data_git_msg = """\
commit 13babd7d1d9ebea34e97b15277ffb1be794ab376
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Jun 8 10:37:11 2022 -0700

    [cleanup] Write a newline into the `latest.txt` file
    
    1. Write a newline into the `latest.txt` file.  This allows a user to
       `cat` this file without it running into their shell prompt configuration.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
