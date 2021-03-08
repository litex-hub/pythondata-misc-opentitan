import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5283"
version_tuple = (0, 0, 5283)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5283")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5188"
data_version_tuple = (0, 0, 5188)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5188")
except ImportError:
    pass
data_git_hash = "d55eaeb0e51b9e2fa79c406fa6328b99f382796a"
data_git_describe = "v0.0-5188-gd55eaeb0e"
data_git_msg = """\
commit d55eaeb0e51b9e2fa79c406fa6328b99f382796a
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Feb 11 12:38:15 2021 -0800

    [spi_device] Command Process block
    
    This commit implements SPI Flash command process block. It decodes first
    8bit of received data and triggers proper downstream module to handle
    the received commands.
    
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
