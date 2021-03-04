import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5234"
version_tuple = (0, 0, 5234)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5234")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5143"
data_version_tuple = (0, 0, 5143)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5143")
except ImportError:
    pass
data_git_hash = "b2576aa8428a553bdbcb8f6ad34377270ea899a8"
data_git_describe = "v0.0-5143-gb2576aa84"
data_git_msg = """\
commit b2576aa8428a553bdbcb8f6ad34377270ea899a8
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Feb 11 19:12:13 2021 -0800

    [dv/lock_reg] Update IPs to adopt the lock_reg changes
    
    Following the lock_reg changes that support reg field, this PR updates
    naming changes to the rest of the DV testbenches.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
