import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14923"
version_tuple = (0, 0, 14923)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14923")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14781"
data_version_tuple = (0, 0, 14781)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14781")
except ImportError:
    pass
data_git_hash = "c74963e3e06eedf3f2870f5d2be570db9302ac6f"
data_git_describe = "v0.0-14781-gc74963e3e0"
data_git_msg = """\
commit c74963e3e06eedf3f2870f5d2be570db9302ac6f
Author: Michael Schaffner <msf@google.com>
Date:   Tue Oct 11 17:59:35 2022 -0700

    [top/test] Add chip_rv_dm_lc_disabled test
    
    This addresses #14147.
    
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
