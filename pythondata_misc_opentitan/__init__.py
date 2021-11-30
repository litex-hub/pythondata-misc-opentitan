import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8885"
version_tuple = (0, 0, 8885)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8885")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8773"
data_version_tuple = (0, 0, 8773)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8773")
except ImportError:
    pass
data_git_hash = "57751de32b7bbe2271c2e8acb54a90ad72309aea"
data_git_describe = "v0.0-8773-g57751de32"
data_git_msg = """\
commit 57751de32b7bbe2271c2e8acb54a90ad72309aea
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Nov 29 20:09:51 2021 -0800

    [dv/top] Disable ast assertion in stub_cpu mode
    
    Rand write csr `clkexl_sel` would cause this assertion to fail in
    top-level. Disable this assertion only in cpu_stub mode.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
