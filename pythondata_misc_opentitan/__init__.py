import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5504"
version_tuple = (0, 0, 5504)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5504")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5409"
data_version_tuple = (0, 0, 5409)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5409")
except ImportError:
    pass
data_git_hash = "bca085f33c9266121cc50e3290d1b21282fc9090"
data_git_describe = "v0.0-5409-gbca085f33"
data_git_msg = """\
commit bca085f33c9266121cc50e3290d1b21282fc9090
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Mar 19 17:37:22 2021 -0700

    [keymgr] Fix advance state consistency
    
    Address #4899
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
