import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9550"
version_tuple = (0, 0, 9550)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9550")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9428"
data_version_tuple = (0, 0, 9428)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9428")
except ImportError:
    pass
data_git_hash = "7ac4c36d70e956f4c2141028988c3d3f8e12b36b"
data_git_describe = "v0.0-9428-g7ac4c36d7"
data_git_msg = """\
commit 7ac4c36d70e956f4c2141028988c3d3f8e12b36b
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Thu Jan 13 08:56:15 2022 -0800

    [ spi_host, prj ] Update SPI_HOST to D2
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
