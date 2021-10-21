import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8388"
version_tuple = (0, 0, 8388)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8388")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8276"
data_version_tuple = (0, 0, 8276)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8276")
except ImportError:
    pass
data_git_hash = "c87bb33f4cf7fa177244dfb635c3ddc2e72a0ff7"
data_git_describe = "v0.0-8276-gc87bb33f4"
data_git_msg = """\
commit c87bb33f4cf7fa177244dfb635c3ddc2e72a0ff7
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Oct 16 10:27:45 2021 -0700

    [spi_host top_earlgrey rtl] Remove secondary core clock
    
    - Removes async tlul fifo from spi_host.sv
    - Identifies all "core" clocks and resets as the same as the bus clock
    - Modifies top_earlgrey xbar_peri to place the two spi_host instances on
      their appropriate clock domains
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
