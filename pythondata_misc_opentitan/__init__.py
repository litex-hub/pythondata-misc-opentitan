import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5315"
version_tuple = (0, 0, 5315)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5315")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5220"
data_version_tuple = (0, 0, 5220)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5220")
except ImportError:
    pass
data_git_hash = "e3af4cf067cbf39261a08ab1421789b907f2fb0f"
data_git_describe = "v0.0-5220-ge3af4cf06"
data_git_msg = """\
commit e3af4cf067cbf39261a08ab1421789b907f2fb0f
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Mar 9 17:22:01 2021 -0800

    [dvsim] Fix for #5527
    
    Ignore `--remote` if `--dry-run` is passed.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
