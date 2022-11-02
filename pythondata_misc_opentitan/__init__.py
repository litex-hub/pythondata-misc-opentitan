import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15140"
version_tuple = (0, 0, 15140)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15140")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14998"
data_version_tuple = (0, 0, 14998)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14998")
except ImportError:
    pass
data_git_hash = "0526196043521f6610e36d9d0e98c1326230639a"
data_git_describe = "v0.0-14998-g0526196043"
data_git_msg = """\
commit 0526196043521f6610e36d9d0e98c1326230639a
Author: Abdullah Varici <abdullah.varici@lowrisc.org>
Date:   Wed Oct 26 20:06:53 2022 +0100

    [top-level/pwrmgr] Extend chip_sw_pwrmgr_main_power_glitch_reset
    
    Add three groups of assertions to check that:
    - the clock valids are deasserted if a power glitch is detected.
    - clocks are stopped if their valid is deasserted.
    - clocks are running if their valid is asserted.
    Enable pwrmgr_ast_sva_if.sv assertions in _vseq file.
    Add main_, io_, usb_ clock inputs to pwrmgr_ast_sva_if and
    create a binding in tb.sv for that.
    
    Signed-off-by: Abdullah Varici <abdullah.varici@lowrisc.org>

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
