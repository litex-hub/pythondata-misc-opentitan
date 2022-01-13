import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9497"
version_tuple = (0, 0, 9497)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9497")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9379"
data_version_tuple = (0, 0, 9379)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9379")
except ImportError:
    pass
data_git_hash = "0416df9b9e2d1d167efb56e0a8dd11eab2a98cbd"
data_git_describe = "v0.0-9379-g0416df9b9"
data_git_msg = """\
commit 0416df9b9e2d1d167efb56e0a8dd11eab2a98cbd
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Mon Jan 3 15:38:46 2022 -0800

    [ spi_host, rtl/dv/doc ] New "OUTPUT_EN" register
    
    - All SPI_HOST outputs are now disabled by default until the OUTPUT_EN register is set
    - Includes a one line change to the SPI_HOST DV environment to activate this
    - A description of the new register field has been added to the documentation
    
    Fixes 8920
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
