import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5436"
version_tuple = (0, 0, 5436)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5436")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5341"
data_version_tuple = (0, 0, 5341)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5341")
except ImportError:
    pass
data_git_hash = "0a49c7e5da806b8c202e446114f371c20ce29d01"
data_git_describe = "v0.0-5341-g0a49c7e5d"
data_git_msg = """\
commit 0a49c7e5da806b8c202e446114f371c20ce29d01
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Mar 17 10:21:36 2021 -0700

    [spi_device] Remove cmdparse until read command path implemented
    
    Removing cmdparse temporary until readcmd path is implemented and
    checked in the synthesis tool.
    
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
