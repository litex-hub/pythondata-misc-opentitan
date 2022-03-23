import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11035"
version_tuple = (0, 0, 11035)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11035")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10909"
data_version_tuple = (0, 0, 10909)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10909")
except ImportError:
    pass
data_git_hash = "18cde68b2f3689f79a320f3006f84f06d33513e1"
data_git_describe = "v0.0-10909-g18cde68b2"
data_git_msg = """\
commit 18cde68b2f3689f79a320f3006f84f06d33513e1
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Mar 1 17:11:13 2022 +0000

    [sw,crypto] Adjust cryptolib drivers to use abs_mmio.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
