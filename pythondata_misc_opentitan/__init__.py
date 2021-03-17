import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5437"
version_tuple = (0, 0, 5437)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5437")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5342"
data_version_tuple = (0, 0, 5342)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5342")
except ImportError:
    pass
data_git_hash = "6f98f3534462701e3bdbe0585782087a3f7a6dcc"
data_git_describe = "v0.0-5342-g6f98f3534"
data_git_msg = """\
commit 6f98f3534462701e3bdbe0585782087a3f7a6dcc
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 10 16:27:29 2021 -0800

    [top, dcd] top and dcd updates for integration
    
    - tie off dcd unused signals
    - slight rename of inter-module ports
    - hook-up in top_earlgrey.hjson
    - hook-up to ast
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [sw] updates to plic / pwrmgr dif unit tests
    
    - increase interrupt number
    - update wakeup reasons
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top] Auto generate files
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [dcd] remove non-ascii characters
    
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
