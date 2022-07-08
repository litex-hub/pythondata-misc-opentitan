import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12974"
version_tuple = (0, 0, 12974)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12974")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12832"
data_version_tuple = (0, 0, 12832)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12832")
except ImportError:
    pass
data_git_hash = "c0a96f9b46e96aa83a2db0469383067c36fcb5e8"
data_git_describe = "v0.0-12832-gc0a96f9b46"
data_git_msg = """\
commit c0a96f9b46e96aa83a2db0469383067c36fcb5e8
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jul 7 15:05:10 2022 -0700

    [dv/alert_handler] Change timeout from actual time to clock cycles
    
    This PR changes the implementation of EDN request timeout check from
    measuring actual time to clock cycles. This is becuase in LPG cases, we
    will stub the clk_i, and it will trigger this timeout check even though
    the clock is stopped.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
