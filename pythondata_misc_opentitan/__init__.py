import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14309"
version_tuple = (0, 0, 14309)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14309")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14167"
data_version_tuple = (0, 0, 14167)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14167")
except ImportError:
    pass
data_git_hash = "f613046ab59dcf5ba23039e456cdc1740b29e030"
data_git_describe = "v0.0-14167-gf613046ab5"
data_git_msg = """\
commit f613046ab59dcf5ba23039e456cdc1740b29e030
Author: Alexander Williams <awill@google.com>
Date:   Mon Sep 19 20:24:06 2022 -0700

    [dv] Update testplan for chip_sw_spi_device_flash_mode
    
    Fill in the test used (chip_sw_uart_tx_rx_bootstrap).
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
