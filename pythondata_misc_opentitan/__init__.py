import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5730"
version_tuple = (0, 0, 5730)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5730")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5635"
data_version_tuple = (0, 0, 5635)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5635")
except ImportError:
    pass
data_git_hash = "eae77096b27abf66eef85dca0e437706cda37eae"
data_git_describe = "v0.0-5635-geae77096b"
data_git_msg = """\
commit eae77096b27abf66eef85dca0e437706cda37eae
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Mar 31 10:45:48 2021 -0700

    [spi] Define Passthrough interface
    
    `passthrough_req/rsp_t` are for SPI passthrough communications between
    SPI_DEVICE and SPI_HOST, more broadly between host system and downstream
    flash device.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
