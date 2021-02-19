import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5048"
version_tuple = (0, 0, 5048)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5048")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4957"
data_version_tuple = (0, 0, 4957)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4957")
except ImportError:
    pass
data_git_hash = "bd80aed965f06a2a2b74e2d469f057c7c88a68bc"
data_git_describe = "v0.0-4957-gbd80aed96"
data_git_msg = """\
commit bd80aed965f06a2a2b74e2d469f057c7c88a68bc
Author: Weicai Yang <weicai@google.com>
Date:   Thu Feb 18 15:51:37 2021 -0800

    [top/dv] Fix uart CSR failure
    
    uart RX pin may not be connected. When loopback is set, TX pin may
    toggle unexpectedly. Disable monitor TX pin in CSR test
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
