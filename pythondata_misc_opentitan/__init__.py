import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8487"
version_tuple = (0, 0, 8487)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8487")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8375"
data_version_tuple = (0, 0, 8375)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8375")
except ImportError:
    pass
data_git_hash = "351ff1a4dfb698171f0c4d684c2309d75961318e"
data_git_describe = "v0.0-8375-g351ff1a4d"
data_git_msg = """\
commit 351ff1a4dfb698171f0c4d684c2309d75961318e
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Oct 27 20:50:19 2021 +0000

    [spi_device] CmdInfo to have valid field
    
    Previous command info list does not have the entry valid field. So the
    HW logic always assumes the info config is valid. It means from the SW
    point of view, SW shall program entire lists regardless of its use.
    
    This PR introduces valid field in the command info entry and HW only
    use valid entries.
    
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
