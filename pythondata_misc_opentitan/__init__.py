import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15229"
version_tuple = (0, 0, 15229)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15229")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15087"
data_version_tuple = (0, 0, 15087)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15087")
except ImportError:
    pass
data_git_hash = "3ca5d009499e5b96d7f685c11986e6dc3f9fa497"
data_git_describe = "v0.0-15087-g3ca5d00949"
data_git_msg = """\
commit 3ca5d009499e5b96d7f685c11986e6dc3f9fa497
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Nov 3 21:50:08 2022 -0700

    [chip dv] Fixes for chip_csr_aliasing and outstanding tests
    
    Increase the simulated time and wall clock time timeouts.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
