import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8306"
version_tuple = (0, 0, 8306)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8306")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8194"
data_version_tuple = (0, 0, 8194)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8194")
except ImportError:
    pass
data_git_hash = "055ac9ddf5952084b4eb50ff0b4f7cf246a6d53c"
data_git_describe = "v0.0-8194-g055ac9ddf"
data_git_msg = """\
commit 055ac9ddf5952084b4eb50ff0b4f7cf246a6d53c
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Oct 14 23:14:11 2021 +0000

    [dif/clkmgr] Moved HW config checks to static asserts.
    
    Some HW configuration checks were done unnecessarily within a DIF vs. as
    a static_assert. This fixes that mistake, as pointed out in #8661.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
