import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8145"
version_tuple = (0, 0, 8145)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8145")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8037"
data_version_tuple = (0, 0, 8037)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8037")
except ImportError:
    pass
data_git_hash = "0e52c6a93de00f717e46262a1e9be8cd302918c8"
data_git_describe = "v0.0-8037-g0e52c6a93"
data_git_msg = """\
commit 0e52c6a93de00f717e46262a1e9be8cd302918c8
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Sep 15 17:00:20 2021 -0700

    [spi_device] TPM pre-dv
    
    This commit scaffolds the TPM over SPI pre-dv tests.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post108"
tool_version_tuple = (0, 0, 108)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post108")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
