import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8228"
version_tuple = (0, 0, 8228)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8228")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8116"
data_version_tuple = (0, 0, 8116)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8116")
except ImportError:
    pass
data_git_hash = "cb6c456456939d77589c65a40d2c907a7dd30486"
data_git_describe = "v0.0-8116-gcb6c45645"
data_git_msg = """\
commit cb6c456456939d77589c65a40d2c907a7dd30486
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Mon Oct 11 16:40:34 2021 -0700

    [spi_host, rtl] Clarify transitions for "bypassable" idle states
    
    The SPI_HOST idle states `Idle` and `IdleCSBActive` are bypassable, meaning if
    their exit condition is satisfied, the FSM can transition immediately from the
    pre-idle to the next post-idle state. (See the SPI_HOST specification for more
    details.)
    
    This commit simply refactors the previous implementation for better clarity and
    robustness.
    
    Prior to this commit there was duplicated code in both the idle states,
    as well as their preceding states.  This makes the code both harder to
    follow and more bug-prone, as disparate edits can be made in either place.
    
    This commit adds new signals: state_after_idle and state_after_idle_csb_active
    to compute the next state when the exit condition for both states.
    These signals are then explicitly examined in the pre-idle state to
    perform the idle-bypass if appropriate.
    
    A bypass can only occur if command_ready is asserted, the command_ready
    signal is also asserted up to one clock cycle before entering an idle state
    So the always_comb blocks that compute state_after_idle_csb_active therefore
    also perform the neccesary computation for the command_ready signal.  Which is
    somewhat complex because of the possibility of an aborted CSAAT segment.
    (command_ready is always high in the idle state or one cycle before the
    idle state)
    
    ----
    
    In addition this commit changes how configuration changes are identified.
    Previously a configuration change was assumed to happen only when CSID changed
    between two command segments.  The FSM now also checks for any changes in the
    configopts structure passed in with the command segment.
    
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
