import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10839"
version_tuple = (0, 0, 10839)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10839")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10713"
data_version_tuple = (0, 0, 10713)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10713")
except ImportError:
    pass
data_git_hash = "aa4ade1ae62e31d40ad4ea7301998b51f4764515"
data_git_describe = "v0.0-10713-gaa4ade1ae"
data_git_msg = """\
commit aa4ade1ae62e31d40ad4ea7301998b51f4764515
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Mar 10 17:09:35 2022 -0800

    [spi_device] Adding sck_ prefix
    
    To clarify the signal clock domain, adding `sck_` to the BUSY set and
    broadcast signal.
    
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
