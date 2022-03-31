import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11255"
version_tuple = (0, 0, 11255)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11255")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11129"
data_version_tuple = (0, 0, 11129)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11129")
except ImportError:
    pass
data_git_hash = "47854c7edecab6f0f95c122a7cbab52368984e46"
data_git_describe = "v0.0-11129-g47854c7ed"
data_git_msg = """\
commit 47854c7edecab6f0f95c122a7cbab52368984e46
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 31 09:52:40 2022 +0100

    [otbn] Declare V2
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
