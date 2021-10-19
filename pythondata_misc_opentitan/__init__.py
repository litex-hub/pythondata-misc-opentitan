import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8332"
version_tuple = (0, 0, 8332)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8332")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8220"
data_version_tuple = (0, 0, 8220)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8220")
except ImportError:
    pass
data_git_hash = "777ecae1d5476c5004920b756e99173d0ae28e6a"
data_git_describe = "v0.0-8220-g777ecae1d"
data_git_msg = """\
commit 777ecae1d5476c5004920b756e99173d0ae28e6a
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Oct 18 18:28:29 2021 -0700

    [chip,dv] Fix SW GPIO smoketest failure
    
    The test was failing in regr with a NOA error. Made the following fixes:
    - Enhanced sw_test_status_if.sv to have a notion of SW test iterations
    (test vseq can reboot the chip multiple times)
    - Fixed accidental byte swap in gpio smoke vseq
    - Other associated fixes
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
