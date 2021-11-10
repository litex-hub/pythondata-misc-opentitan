import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8662"
version_tuple = (0, 0, 8662)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8662")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8550"
data_version_tuple = (0, 0, 8550)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8550")
except ImportError:
    pass
data_git_hash = "8e5c0aec13ab9a6faed5903d335cb64da8ca0d68"
data_git_describe = "v0.0-8550-g8e5c0aec1"
data_git_msg = """\
commit 8e5c0aec13ab9a6faed5903d335cb64da8ca0d68
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Fri Oct 22 17:12:22 2021 +0100

    [sw, tests] Introduce "chip_sw_sram_execution" Main SRAM test
    
    The test is described here:
    https://docs.opentitan.org/hw/top_earlgrey/doc/dv/
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
