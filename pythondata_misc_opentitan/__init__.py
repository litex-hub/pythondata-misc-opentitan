import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8621"
version_tuple = (0, 0, 8621)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8621")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8509"
data_version_tuple = (0, 0, 8509)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8509")
except ImportError:
    pass
data_git_hash = "8be44c91f64b8ade77966ac786b70d31051fd6b3"
data_git_describe = "v0.0-8509-g8be44c91f"
data_git_msg = """\
commit 8be44c91f64b8ade77966ac786b70d31051fd6b3
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Oct 20 16:50:56 2021 -0700

    [clkmgr, ast] Update external clock switch support
    
    Support external clock switch based on most recent Nuvoton request
    Fixes #8657
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [clkmgr] Address some cdc issues on step_down_req/ack
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [clkmgr, top] rebase updates for external clock switch support
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
