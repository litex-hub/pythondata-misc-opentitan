import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5238"
version_tuple = (0, 0, 5238)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5238")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5147"
data_version_tuple = (0, 0, 5147)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5147")
except ImportError:
    pass
data_git_hash = "6d49f60b55f8453df208034e43c6ce64b33e04ba"
data_git_describe = "v0.0-5147-g6d49f60b5"
data_git_msg = """\
commit 6d49f60b55f8453df208034e43c6ce64b33e04ba
Author: Tung Hoang <hoang.tung@wdc.com>
Date:   Sun Feb 28 10:34:49 2021 -0800

    [spi_device, dv] Refactor spi_agent to support spi_host rtl
    
      - Extend spi_if to provide 4 channels required by spi_host rtl
      - Replace uni-direction sdi and sdo ports by bi-direction sio ports in spi_if
      - Update spi_device and top_earlgrey testbench with new ports
    
    Signed-off-by: Tung Hoang <hoang.tung@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
