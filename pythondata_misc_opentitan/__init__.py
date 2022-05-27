import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12382"
version_tuple = (0, 0, 12382)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12382")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12242"
data_version_tuple = (0, 0, 12242)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12242")
except ImportError:
    pass
data_git_hash = "595576b22ee9a1c04046815b44702b1f5c5f2ba1"
data_git_describe = "v0.0-12242-g595576b22"
data_git_msg = """\
commit 595576b22ee9a1c04046815b44702b1f5c5f2ba1
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu May 26 10:58:05 2022 -0700

    chore(cdc): Waive pads attribute to multiple clocks
    
    pads dio attribute config crosses multiple clocks (IO_DIV4 -> {USB,
    AON}). However, the attributes are static signals. Also, the receivers
    have synchronizers too. As each IP is unique, there's no reconvergence
    issue.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
