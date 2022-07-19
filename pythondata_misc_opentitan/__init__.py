import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13176"
version_tuple = (0, 0, 13176)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13176")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13034"
data_version_tuple = (0, 0, 13034)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13034")
except ImportError:
    pass
data_git_hash = "7365f25f56928f457e2d6a61fa96eaf8398730b9"
data_git_describe = "v0.0-13034-g7365f25f56"
data_git_msg = """\
commit 7365f25f56928f457e2d6a61fa96eaf8398730b9
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Thu Jul 14 16:35:38 2022 +0000

    [flash_ctrl,dv] single bit error test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
