import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8585"
version_tuple = (0, 0, 8585)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8585")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8473"
data_version_tuple = (0, 0, 8473)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8473")
except ImportError:
    pass
data_git_hash = "b423419ab18fc194dfecd13e8ccfc7899e981645"
data_git_describe = "v0.0-8473-gb423419ab"
data_git_msg = """\
commit b423419ab18fc194dfecd13e8ccfc7899e981645
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Oct 29 00:21:29 2021 -0700

    [chip testplan] Make SRAM exec test comprehensive
    
    Mandates the need to test execution enablement in all 8 scenarios
    resulting from HW_CFG[IFETCH} bit in OTP controller, HW_DEBUG_EN LC
    state and the execution enable CSR value, for both main and retention
    SRAMs.
    
    This is captured as one testpoint since the SW test portion will more or
    less remain the same. It could be split into 4 tests which each variant
    creating the right scenario via backdoor from the testbench side (TBD).
    
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
