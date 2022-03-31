import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11264"
version_tuple = (0, 0, 11264)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11264")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11138"
data_version_tuple = (0, 0, 11138)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11138")
except ImportError:
    pass
data_git_hash = "1ab19709303e86c3ecfe544bf2f922f5d245fc7d"
data_git_describe = "v0.0-11138-g1ab197093"
data_git_msg = """\
commit 1ab19709303e86c3ecfe544bf2f922f5d245fc7d
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Mar 30 17:12:38 2022 -0700

    [spi_device] TB skeleton for Read SFDP
    
    This commit adds a simple SPI flash command to fetch 4 Bytes via Read
    SFDP command.
    
    The return data as of now is not correct.
    
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
