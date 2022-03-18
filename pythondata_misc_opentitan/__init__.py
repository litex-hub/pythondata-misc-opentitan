import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10967"
version_tuple = (0, 0, 10967)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10967")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10841"
data_version_tuple = (0, 0, 10841)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10841")
except ImportError:
    pass
data_git_hash = "01e039027fa097ba6bf374e1f4338a729b39bab4"
data_git_describe = "v0.0-10841-g01e039027"
data_git_msg = """\
commit 01e039027fa097ba6bf374e1f4338a729b39bab4
Author: Weicai Yang <weicai@google.com>
Date:   Thu Mar 17 13:52:03 2022 -0700

    [keymgr/dv] Update otp key sample point
    
    Updated to sample it when starting advance operation at StInit
    
    Aligned with design update at #11459
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
