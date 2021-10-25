import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8435"
version_tuple = (0, 0, 8435)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8435")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8323"
data_version_tuple = (0, 0, 8323)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8323")
except ImportError:
    pass
data_git_hash = "b9fcaae85ab87bf1cc90708018d3678380b409c1"
data_git_describe = "v0.0-8323-gb9fcaae85"
data_git_msg = """\
commit b9fcaae85ab87bf1cc90708018d3678380b409c1
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Oct 25 11:26:54 2021 -0700

    [conn] Update spi_host clk
    
    With PR #8709, the clk_core_i is removed from SPI_HOST.
    So update the connectivity test to reflect the change.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
