import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8720"
version_tuple = (0, 0, 8720)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8720")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8608"
data_version_tuple = (0, 0, 8608)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8608")
except ImportError:
    pass
data_git_hash = "4c51f91c905e67c3754d1354f2d2b18dadc95598"
data_git_describe = "v0.0-8608-g4c51f91c9"
data_git_msg = """\
commit 4c51f91c905e67c3754d1354f2d2b18dadc95598
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Mon Nov 15 17:29:57 2021 +0000

    [spi_device] Add INTERCEPT_EN CSR
    
    This commit adds INTERCEPT_EN CSR to SPI_DEVICE.
    The CSR allows SW to assume the Passthrough SPI selectively. If assumed,
    the command is processed internally and returned to the host system.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
