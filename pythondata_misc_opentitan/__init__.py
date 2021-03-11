import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5330"
version_tuple = (0, 0, 5330)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5330")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5235"
data_version_tuple = (0, 0, 5235)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5235")
except ImportError:
    pass
data_git_hash = "2612b256efd3a88bf607c195efa2ac838216d2d7"
data_git_describe = "v0.0-5235-g2612b256e"
data_git_msg = """\
commit 2612b256efd3a88bf607c195efa2ac838216d2d7
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 10 14:11:26 2021 -0800

    [keymgr] latch one-hot error when it happens
    
    Address #5363
    
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
