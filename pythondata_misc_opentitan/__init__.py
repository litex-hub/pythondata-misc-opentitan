import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5327"
version_tuple = (0, 0, 5327)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5327")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5232"
data_version_tuple = (0, 0, 5232)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5232")
except ImportError:
    pass
data_git_hash = "a12231dfc6e370977242d0f18ecf36f7d6816b52"
data_git_describe = "v0.0-5232-ga12231dfc"
data_git_msg = """\
commit a12231dfc6e370977242d0f18ecf36f7d6816b52
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Mar 9 13:49:50 2021 -0800

    [spi_device] Move modules inside fwmode
    
    Move FwMode related modules inside fwmode submodules to be
    self-contained and to increase readability.
    
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
