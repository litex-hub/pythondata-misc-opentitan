import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13145"
version_tuple = (0, 0, 13145)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13145")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13003"
data_version_tuple = (0, 0, 13003)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13003")
except ImportError:
    pass
data_git_hash = "62c05c026f8a54b136066c634788fa3e6746c8c5"
data_git_describe = "v0.0-13003-g62c05c026f"
data_git_msg = """\
commit 62c05c026f8a54b136066c634788fa3e6746c8c5
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Tue Jul 12 18:22:15 2022 +0000

    [dv,flash_ctrl] remove scb_set_exp_alert
    
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
