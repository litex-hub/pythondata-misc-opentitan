import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10901"
version_tuple = (0, 0, 10901)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10901")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10775"
data_version_tuple = (0, 0, 10775)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10775")
except ImportError:
    pass
data_git_hash = "d1f4de94d527b90e4950e3cf1773cb3b10ff8df8"
data_git_describe = "v0.0-10775-gd1f4de94d"
data_git_msg = """\
commit d1f4de94d527b90e4950e3cf1773cb3b10ff8df8
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Mon Mar 14 19:55:12 2022 -0700

    [spi_device] Move CSb edge detector to top
    
    This commit moves CSb synchronizer and assertion/ de-assertion checker
    to the SPI_DEVICE TOP. The synchronizer and edge detectors have existed
    at the TOP module already. This commit is to combine the synchronizer to
    the TOP so that it removes chance of reconvergence issues.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
