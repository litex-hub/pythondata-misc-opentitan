import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12741"
version_tuple = (0, 0, 12741)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12741")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12599"
data_version_tuple = (0, 0, 12599)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12599")
except ImportError:
    pass
data_git_hash = "f4ca836484b51ab398b67bbe0294bc9493fb66f5"
data_git_describe = "v0.0-12599-gf4ca836484"
data_git_msg = """\
commit f4ca836484b51ab398b67bbe0294bc9493fb66f5
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jun 13 13:47:22 2022 +0200

    [top, fpga] Align Ibex configuration for English Breakfast
    
    This commit re-enables the BT ALU and WB stage on the CW305 (both
    options help improving performance when using software PRNGs for SCA
    experiments) and moves the disabling of the instruction cache to the
    top hjson file to align the Verilator simulation with the FPGA.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
