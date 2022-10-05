import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14564"
version_tuple = (0, 0, 14564)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14564")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14422"
data_version_tuple = (0, 0, 14422)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14422")
except ImportError:
    pass
data_git_hash = "88ca99f0457064f0df25149b87f3bffaa421eb44"
data_git_describe = "v0.0-14422-g88ca99f045"
data_git_msg = """\
commit 88ca99f0457064f0df25149b87f3bffaa421eb44
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Sep 28 19:59:09 2022 -0700

    [ottool] Add some simple annotations
    
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
