import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5339"
version_tuple = (0, 0, 5339)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5339")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5244"
data_version_tuple = (0, 0, 5244)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5244")
except ImportError:
    pass
data_git_hash = "a0c880dff8b1a941c4e7dcf0f60342b0a7ec4075"
data_git_describe = "v0.0-5244-ga0c880dff"
data_git_msg = """\
commit a0c880dff8b1a941c4e7dcf0f60342b0a7ec4075
Author: Eric Shiu <eshiu@google.com>
Date:   Tue Mar 9 15:45:07 2021 -0800

    [dcd] Added new IP to top lint config
    
    Signed-off-by: Eric Shiu <eshiu@google.com>

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
