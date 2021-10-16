import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8312"
version_tuple = (0, 0, 8312)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8312")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8200"
data_version_tuple = (0, 0, 8200)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8200")
except ImportError:
    pass
data_git_hash = "4ac735964069019021cab557d39f363691b38820"
data_git_describe = "v0.0-8200-g4ac735964"
data_git_msg = """\
commit 4ac735964069019021cab557d39f363691b38820
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Mon Oct 11 18:04:41 2021 -0700

    [spi_host, rtl] Fix/Refactor state wait counters in SPI_HOST FSM
    
    - Fixes a bug in which there was no wait counter associated with the
    CSBSwitch state (it was using the wait_idle counter, but this
    counter was not being appropriately reset on entering CSBSwitch)
    - Refactors the wait_idle, wait_lead, and wait_trail counters
    into a single wait_cntr that can be commonly managed
    - wait_cntr is properly reset up entering the WaitIdle, WaitLead,
    WaitTrail and CSBSwitch states
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
