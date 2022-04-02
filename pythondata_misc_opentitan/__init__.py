import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11314"
version_tuple = (0, 0, 11314)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11314")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11188"
data_version_tuple = (0, 0, 11188)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11188")
except ImportError:
    pass
data_git_hash = "9beba9baf591c2ca438eec49b1c9ffc460af5342"
data_git_describe = "v0.0-11188-g9beba9baf"
data_git_msg = """\
commit 9beba9baf591c2ca438eec49b1c9ffc460af5342
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Apr 1 22:40:51 2022 +0000

    [sw/test_rom] Init SRAM for non-sim_dv devices
    
    In DV sim, the testbench handles the SRAM init via backdoor loading to
    optimize test run time. However, in Verilator and FPGA, this is not the
    case. Therefore to prevent this from causing a bus integrity error, we
    initialize SRAM for Verilator and FPGA devices.
    
    This fixes #11854.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
