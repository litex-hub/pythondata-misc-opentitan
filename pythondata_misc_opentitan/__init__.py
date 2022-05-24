import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12293"
version_tuple = (0, 0, 12293)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12293")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12165"
data_version_tuple = (0, 0, 12165)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12165")
except ImportError:
    pass
data_git_hash = "bc729bb52b153fe236714fa3506f1a7315eb5b4c"
data_git_describe = "v0.0-12165-gbc729bb52"
data_git_msg = """\
commit bc729bb52b153fe236714fa3506f1a7315eb5b4c
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Thu May 19 17:47:51 2022 +0100

    [sw,tests] Test sysrst_ctrl combo detect reset and wakeup
    
    For tests:
    chip_sw_sysrst_ctrl_gsc_reset
    chip_sw_sysrst_ctrl_sleep_gsc_wakeup
    chip_sw_sysrst_ctrl_sleep_gsc_reset
    
    Tests that a specified input pin combination can be detected by the sysrst_ctrl and reset the system.
    Checks that the reset also asserts ec_rst_l when this is set as an action for a combo detect.
    Checks that when a reset condition is entered that flash_wp is also asserted.
    Tests that ULP wakeup in sysrst_ctrl can be triggered with a pin input to wake the system from sleep.
    Tests that when the system is in deep sleep that an input pin combination can be detected and reset the
    system.
    
    Signed-off-by: Dave Williams <dave.williams@ensilica.com>

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
