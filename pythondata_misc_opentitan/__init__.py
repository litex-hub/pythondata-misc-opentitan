import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14864"
version_tuple = (0, 0, 14864)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14864")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14722"
data_version_tuple = (0, 0, 14722)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14722")
except ImportError:
    pass
data_git_hash = "2f668bcd9da6aaa3771b1bc9f3b05f20a6bf7167"
data_git_describe = "v0.0-14722-g2f668bcd9d"
data_git_msg = """\
commit 2f668bcd9da6aaa3771b1bc9f3b05f20a6bf7167
Author: Michael Schaffner <msf@google.com>
Date:   Thu Oct 20 11:38:53 2022 -0700

    [top] Remove defunct synthesis dashboard
    
    The synthesis dashboard is currently not working,
    hence we remove it for the time being.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
