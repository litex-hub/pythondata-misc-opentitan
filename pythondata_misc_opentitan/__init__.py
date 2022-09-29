import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14489"
version_tuple = (0, 0, 14489)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14489")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14347"
data_version_tuple = (0, 0, 14347)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14347")
except ImportError:
    pass
data_git_hash = "62747439226d65a760ec82b90c2da13886e52958"
data_git_describe = "v0.0-14347-g6274743922"
data_git_msg = """\
commit 62747439226d65a760ec82b90c2da13886e52958
Author: Alexander Williams <awill@google.com>
Date:   Wed Sep 28 16:46:12 2022 -0700

    [dv] Adjust chip_sw_uart_tx_rx_bootstrap max sim time
    
    It can go longer than 60 ms, so adjust to 80 ms.
    
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
