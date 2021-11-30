import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8913"
version_tuple = (0, 0, 8913)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8913")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8801"
data_version_tuple = (0, 0, 8801)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8801")
except ImportError:
    pass
data_git_hash = "fffa53a98af538c5a402e06de84243dfe7769610"
data_git_describe = "v0.0-8801-gfffa53a98"
data_git_msg = """\
commit fffa53a98af538c5a402e06de84243dfe7769610
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Nov 29 15:43:13 2021 -0800

    [dv/clkmgr] Fix clkmgr_extclk test
    
    Update the test for updates in the RTL.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
