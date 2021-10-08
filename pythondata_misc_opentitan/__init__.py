import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8191"
version_tuple = (0, 0, 8191)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8191")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8079"
data_version_tuple = (0, 0, 8079)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8079")
except ImportError:
    pass
data_git_hash = "054b24698a73be23a3695ea5f60633ed12d8e72c"
data_git_describe = "v0.0-8079-g054b24698"
data_git_msg = """\
commit 054b24698a73be23a3695ea5f60633ed12d8e72c
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Oct 7 05:41:09 2021 +0000

    [dif/usbdev] Add const qualifier to device handle.
    
    It is typical for the first argument of every DIF to be a pointer to the
    device handle struct. These should be marked const, since DIFs should
    not modify them.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
