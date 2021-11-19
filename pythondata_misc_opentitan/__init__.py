import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8769"
version_tuple = (0, 0, 8769)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8769")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8657"
data_version_tuple = (0, 0, 8657)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8657")
except ImportError:
    pass
data_git_hash = "b0cad3827b4fd804372f36aa331e6480f4c830b5"
data_git_describe = "v0.0-8657-gb0cad3827"
data_git_msg = """\
commit b0cad3827b4fd804372f36aa331e6480f4c830b5
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Nov 18 17:39:33 2021 +0000

    [spi_device] Add Locality related section in TPM
    
    This commit revises the SPI_DEVICE TPM spec to explain how
    TPM_ACCESS_x.activeLocality and received Locality affects the return
    value of the Return-by-HW registers.
    
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
