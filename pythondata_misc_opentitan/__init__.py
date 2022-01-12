import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9463"
version_tuple = (0, 0, 9463)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9463")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9345"
data_version_tuple = (0, 0, 9345)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9345")
except ImportError:
    pass
data_git_hash = "430ef6c2cd84ab6f52b48e28c246de3404a8c6a7"
data_git_describe = "v0.0-9345-g430ef6c2c"
data_git_msg = """\
commit 430ef6c2cd84ab6f52b48e28c246de3404a8c6a7
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Jan 11 18:29:00 2022 -0800

    [sw, dv, device.h] Add symbol for AON clock freq
    
    This PR adds a `device.h` symbol representing AON clock frequency, which
    is set differently in each simulation platform.
    
    Fixes #9927.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
