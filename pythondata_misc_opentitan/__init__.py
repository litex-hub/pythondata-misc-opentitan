import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9916"
version_tuple = (0, 0, 9916)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9916")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9792"
data_version_tuple = (0, 0, 9792)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9792")
except ImportError:
    pass
data_git_hash = "6c29be027779bef87d85d5a69bf1b96afe310f88"
data_git_describe = "v0.0-9792-g6c29be027"
data_git_msg = """\
commit 6c29be027779bef87d85d5a69bf1b96afe310f88
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Jan 28 20:30:29 2022 -0800

    [lc_ctrl] Annotate RTL with CM labels
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
