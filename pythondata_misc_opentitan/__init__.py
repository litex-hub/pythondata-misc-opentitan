import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9667"
version_tuple = (0, 0, 9667)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9667")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9545"
data_version_tuple = (0, 0, 9545)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9545")
except ImportError:
    pass
data_git_hash = "72643363e818f11a292d87913b7b3acc0e002714"
data_git_describe = "v0.0-9545-g72643363e"
data_git_msg = """\
commit 72643363e818f11a292d87913b7b3acc0e002714
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jan 20 10:31:44 2022 -0800

    [dv/otp] Two regression fixes
    
    1). Remove test_access because it is replaced by another tlul interface.
    Actual checking will be done in a separate PR, as we need to ensure it
    does not break vendor tests.
    2). Add a few assertion checks for vendor_test related I/Os. The main
    check should be done in closed-source vendor test.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
