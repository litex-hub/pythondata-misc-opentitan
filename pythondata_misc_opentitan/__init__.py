import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15252"
version_tuple = (0, 0, 15252)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15252")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15110"
data_version_tuple = (0, 0, 15110)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15110")
except ImportError:
    pass
data_git_hash = "a1284fc01b5a8d6c081d458cdcb37ebb48202ef7"
data_git_describe = "v0.0-15110-ga1284fc01b"
data_git_msg = """\
commit a1284fc01b5a8d6c081d458cdcb37ebb48202ef7
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Oct 19 12:19:22 2022 -0700

    [rom-e2e] Complete the asm-init test
    
    1. Update the ChipStartup message exchanged between the riscv core and
       the test harness to include all of the information needed to evaluate
       correct initialization of the chip.
    2. Update the chip_specific_startup DUT program to gather all of the
       required information: lifecycle state, OTP config, ast done bit, clock
       jitter config, entropy config, ePMP, interrupt config and SRAM config.
    3. Evaluate the data from the DUT against the OTP configuration and
       lifecycle state.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
