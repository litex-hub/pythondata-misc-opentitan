import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12855"
version_tuple = (0, 0, 12855)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12855")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12713"
data_version_tuple = (0, 0, 12713)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12713")
except ImportError:
    pass
data_git_hash = "7b8869f7f67463fc0fba65a6413d509565595e98"
data_git_describe = "v0.0-12713-g7b8869f7f6"
data_git_msg = """\
commit 7b8869f7f67463fc0fba65a6413d509565595e98
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon Jun 20 17:20:14 2022 +0000

    [dv,flash_ctrl] sample write / read test
    
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
