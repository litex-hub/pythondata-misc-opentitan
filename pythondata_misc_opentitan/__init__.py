import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5938"
version_tuple = (0, 0, 5938)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5938")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5843"
data_version_tuple = (0, 0, 5843)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5843")
except ImportError:
    pass
data_git_hash = "d5c17ccdf0ce03438350cf6792c1bc1f07060e99"
data_git_describe = "v0.0-5843-gd5c17ccdf"
data_git_msg = """\
commit d5c17ccdf0ce03438350cf6792c1bc1f07060e99
Author: Michael Schaffner <msf@google.com>
Date:   Fri Apr 16 17:12:36 2021 -0700

    [sdc] Correct the clock group constraint
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
