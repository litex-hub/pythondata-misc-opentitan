import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8486"
version_tuple = (0, 0, 8486)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8486")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8374"
data_version_tuple = (0, 0, 8374)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8374")
except ImportError:
    pass
data_git_hash = "aa8026b10cf6c5a06ce61ac66834b16248848f7a"
data_git_describe = "v0.0-8374-gaa8026b10"
data_git_msg = """\
commit aa8026b10cf6c5a06ce61ac66834b16248848f7a
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Oct 27 16:13:06 2021 +0000

    [spi_device] Default reset value for TPM_CAP
    
    SPI_DEVICE TPM_CAP is read-only register to SW. The value is assigned
    from parameter values. The reset value now represents the correct
    parameter values.
    
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
