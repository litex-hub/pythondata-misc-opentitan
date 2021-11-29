import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8877"
version_tuple = (0, 0, 8877)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8877")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8765"
data_version_tuple = (0, 0, 8765)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8765")
except ImportError:
    pass
data_git_hash = "028e3fbb9d3120943810c35e136905cc31077c6a"
data_git_describe = "v0.0-8765-g028e3fbb9"
data_git_msg = """\
commit 028e3fbb9d3120943810c35e136905cc31077c6a
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Nov 23 18:36:24 2021 +0000

    [spi_device] Add prefix to the interrupts
    
    This commit adds mode or distinguishable prefixes to the existing
    interrupts. `generic_` prefix is added to pre-existed interrupts.
    `upload_` and `readbuf_` prefixes are added to the flash/passthrough
    related interrupts.
    
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
