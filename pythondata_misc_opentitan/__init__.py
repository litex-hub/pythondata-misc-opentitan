import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12267"
version_tuple = (0, 0, 12267)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12267")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12139"
data_version_tuple = (0, 0, 12139)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12139")
except ImportError:
    pass
data_git_hash = "11959ccf865d0e320245b7ebca781c3a88952ef5"
data_git_describe = "v0.0-12139-g11959ccf8"
data_git_msg = """\
commit 11959ccf865d0e320245b7ebca781c3a88952ef5
Author: Timothy Chen <timothytim@google.com>
Date:   Fri May 20 11:03:47 2022 -0700

    [dv/top] bypass alert watchdog at the end of test
    
    flash_lc_rw_en tests move to scrap state at the end of the
    test, which causes many alerts to continuously fire.
    
    This run option just tells the test to ignore those continuously
    firing alerts.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
