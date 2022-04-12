import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11539"
version_tuple = (0, 0, 11539)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11539")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11413"
data_version_tuple = (0, 0, 11413)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11413")
except ImportError:
    pass
data_git_hash = "6fbcf741bd43222abc75227dde7ef9e80483df80"
data_git_describe = "v0.0-11413-g6fbcf741b"
data_git_msg = """\
commit 6fbcf741bd43222abc75227dde7ef9e80483df80
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Apr 7 11:16:11 2022 -0700

    [dv/chip] Add alert_ping_timeout test
    
    This PR adds an aler_ping_timeout test in chip-level.
    As the testplan describes, this test will configure the alert ping
    timeout to a very small value - 2 cycles, and expect the alert ping to
    always timeout. Then we will check if the interrupt is triggered
    correctly, and if the local alert cause is correct.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
