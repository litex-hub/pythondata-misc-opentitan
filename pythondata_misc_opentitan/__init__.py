import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5656"
version_tuple = (0, 0, 5656)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5656")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5561"
data_version_tuple = (0, 0, 5561)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5561")
except ImportError:
    pass
data_git_hash = "0eefaf1aebe450ea71e2ddc370dea85964f684fb"
data_git_describe = "v0.0-5561-g0eefaf1ae"
data_git_msg = """\
commit 0eefaf1aebe450ea71e2ddc370dea85964f684fb
Author: Tung Hoang <hoang.tung@wdc.com>
Date:   Fri Mar 26 10:51:53 2021 -0700

    [i2c, dv] Refactor i2c_agent to support dual-mode (host and target) dut
    
      - Remove separerate i2c_device/host_driver and i2c_device/host_seq,
        only use i2c_driver/i2c_base_seq for the dual-mode dut
      - Add knob control to i2c_driver and i2c_base_seq
      - Update test to setup the dual-mode dut
      - Clean up code
    
    Signed-off-by: Tung Hoang <hoang.tung@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
