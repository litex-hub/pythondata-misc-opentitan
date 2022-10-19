import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14826"
version_tuple = (0, 0, 14826)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14826")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14684"
data_version_tuple = (0, 0, 14684)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14684")
except ImportError:
    pass
data_git_hash = "8db8bd5b11f42097de0060e63a58fad760a0c923"
data_git_describe = "v0.0-14684-g8db8bd5b11"
data_git_msg = """\
commit 8db8bd5b11f42097de0060e63a58fad760a0c923
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Oct 14 12:03:22 2022 -0400

    [test] Add rom_e2e_boot_policy_bad_manifest
    
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
