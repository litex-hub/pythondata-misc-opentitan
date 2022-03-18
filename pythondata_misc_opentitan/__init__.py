import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10972"
version_tuple = (0, 0, 10972)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10972")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10846"
data_version_tuple = (0, 0, 10846)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10846")
except ImportError:
    pass
data_git_hash = "9c6dff79adc5ff2ccd33bd16e85bfabbafe920c1"
data_git_describe = "v0.0-10846-g9c6dff79a"
data_git_msg = """\
commit 9c6dff79adc5ff2ccd33bd16e85bfabbafe920c1
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Thu Mar 17 03:57:41 2022 -0700

    [dv] enable tlul_assert for csr part2
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
