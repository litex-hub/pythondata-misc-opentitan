import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8213"
version_tuple = (0, 0, 8213)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8213")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8101"
data_version_tuple = (0, 0, 8101)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8101")
except ImportError:
    pass
data_git_hash = "1a6053dc5b759da3d5523889ada1b994de1c892d"
data_git_describe = "v0.0-8101-g1a6053dc5"
data_git_msg = """\
commit 1a6053dc5b759da3d5523889ada1b994de1c892d
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Mon Oct 11 03:50:07 2021 -0700

    [ spi_host, rtl ] Simplify SPI_HOST FSM stall behavior
    
    - Reverts changes to core state variables made in #7377
        - No more "actual" or "prestall" state
    
    Still correctly solves errors noted in #7281 with the following changes:
    - Adds signal command_ready_int to internally track non-stall-condition values
      for command_ready_o
    - Internal signal new_command now depends on command_ready_int, not command_ready_o
    - command_ready_o is masked to always output 0 during a stall condition.
    - All registers and output signals are now enabled only when !stall
    - The name of the state register has been renamed to simply "state_d/q"
    
    This results in a far simpler scheme for managing the FSM, with fewer coverage points
    to worry about.  The previous version, though functional, left some uncertainty as
    to how to establish coverage points for the "actual" and "prestall" states.
    
    - Removes corresponding TODOs from the documentation
    
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
