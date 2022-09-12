import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14117"
version_tuple = (0, 0, 14117)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14117")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13975"
data_version_tuple = (0, 0, 13975)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13975")
except ImportError:
    pass
data_git_hash = "bccbd2cf9d7ab53506a1fa7e88c7d77b9c1baeb3"
data_git_describe = "v0.0-13975-gbccbd2cf9d"
data_git_msg = """\
commit bccbd2cf9d7ab53506a1fa7e88c7d77b9c1baeb3
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Sep 8 11:37:50 2022 -0400

    [opentitanlib] Update FixedSizeBigInt to_bytes methods to return BYTE_LEN long vectors
    
    Fixes #14863
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
