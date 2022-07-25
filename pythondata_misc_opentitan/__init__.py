import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13258"
version_tuple = (0, 0, 13258)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13258")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13116"
data_version_tuple = (0, 0, 13116)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13116")
except ImportError:
    pass
data_git_hash = "1236bb1b0e800d5c06a41fc01884a9d5ac65f739"
data_git_describe = "v0.0-13116-g1236bb1b0e"
data_git_msg = """\
commit 1236bb1b0e800d5c06a41fc01884a9d5ac65f739
Author: Weicai Yang <weicai@google.com>
Date:   Fri Jul 22 12:42:31 2022 -0700

    [spi_device/dv] TPM mode fixes
    
    1. Fix bit order, it supports order 0 rather than 1
    2. Fix CMD code
    3. Add DV_SPINWAIT for while-loop
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
