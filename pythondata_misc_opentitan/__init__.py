import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5765"
version_tuple = (0, 0, 5765)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5765")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5670"
data_version_tuple = (0, 0, 5670)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5670")
except ImportError:
    pass
data_git_hash = "74c4ff235ba08caef2e970f98e0efd1318daea4a"
data_git_describe = "v0.0-5670-g74c4ff235"
data_git_msg = """\
commit 74c4ff235ba08caef2e970f98e0efd1318daea4a
Author: Michael Schaffner <msf@google.com>
Date:   Tue Mar 30 15:43:46 2021 -0700

    [topgen] Rework pinmux datastructure and templatize tops
    
    This is a complete overhaul of the pinmux / padctrl configuration
    datastructure in the top Hjson.
    
    The new datastructures are used to provide more control over the
    DIO/MIO configuration, pinout and target-specific differences
    (ASIC vs FPGA vs Verilator).
    
    The chip-level files are now generated from one common template,
    and all regular DIO/MIO connections are made automatically.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
