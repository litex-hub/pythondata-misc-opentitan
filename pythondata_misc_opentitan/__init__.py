import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8194"
version_tuple = (0, 0, 8194)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8194")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8082"
data_version_tuple = (0, 0, 8082)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8082")
except ImportError:
    pass
data_git_hash = "8fafdc2a3f3d533ddcd7f725475475301cdebf62"
data_git_describe = "v0.0-8082-g8fafdc2a3"
data_git_msg = """\
commit 8fafdc2a3f3d533ddcd7f725475475301cdebf62
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Oct 7 00:50:40 2021 -0700

    [chip,dv,sw] Add SW timeout functionality
    
    This commit adds 2 inlined functions in `ibex.h` to support a timeout
    detection capability. The timeout is set in microseconds.
    
    In addition, it adds a convenience macro that spins on an external
    expression, throwing an error and aborting immediately if the timeout
    occurred waiting for that expression to be true.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
