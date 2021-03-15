import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5393"
version_tuple = (0, 0, 5393)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5393")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5298"
data_version_tuple = (0, 0, 5298)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5298")
except ImportError:
    pass
data_git_hash = "39a1b96b800d7b1f96fbfd368012c64ff0e867d3"
data_git_describe = "v0.0-5298-g39a1b96b8"
data_git_msg = """\
commit 39a1b96b800d7b1f96fbfd368012c64ff0e867d3
Author: Tung Hoang <hoang.tung@wdc.com>
Date:   Thu Feb 25 19:02:21 2021 -0800

    [spi_host, dv] Add spi_host_testplan.hjson
    
    Signed-off-by: Tung Hoang <hoang.tung@wdc.com>

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
