import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8308"
version_tuple = (0, 0, 8308)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8308")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8196"
data_version_tuple = (0, 0, 8196)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8196")
except ImportError:
    pass
data_git_hash = "d7f00ea49fe2eea5bebf6d1e579f9f5b582d3438"
data_git_describe = "v0.0-8196-gd7f00ea49"
data_git_msg = """\
commit d7f00ea49fe2eea5bebf6d1e579f9f5b582d3438
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Oct 14 14:52:00 2021 -0700

    [rstmgr/pwrmgr] Allow software to directly request device reset
    
    - Fixes #8285
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [sw] Add a simple software test case
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top] Auto generate
    
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
