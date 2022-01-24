import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9741"
version_tuple = (0, 0, 9741)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9741")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9619"
data_version_tuple = (0, 0, 9619)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9619")
except ImportError:
    pass
data_git_hash = "8f0feb009e547da8bde9f228403eed2f50ac8ba5"
data_git_describe = "v0.0-9619-g8f0feb009"
data_git_msg = """\
commit 8f0feb009e547da8bde9f228403eed2f50ac8ba5
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Jan 19 01:04:13 2022 -0800

    [chip dv] Fix plic_all_irqs_test for Verilator
    
    ...and FPGA.
    
    The logging mechanism which uses UART0 in Verilator and FPGA setups
    messes up this test, which is meant to enable and test ALL interrupts
    from all peripherals in the device, including UART0. The fix is to skip
    testing UART0 interrupts for Verilator and FPGA.
    
    Fixes #8656.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
