import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14619"
version_tuple = (0, 0, 14619)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14619")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14477"
data_version_tuple = (0, 0, 14477)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14477")
except ImportError:
    pass
data_git_hash = "df662bf3dee4df9b99296054a139daee867153d5"
data_git_describe = "v0.0-14477-gdf662bf3de"
data_git_msg = """\
commit df662bf3dee4df9b99296054a139daee867153d5
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Sep 28 21:44:38 2022 -0700

    [dv/pwrmgr] Fixes for recent RTL changes
    
    The change in handling of reset had a big impact on DV.
    Some test sequences need to be adjusted to stop during lc reset or clock
    stops, and reset handling needs to change.
    The pwrmgr_clk_ctrl_agent was out of sync with the counterpart in
    pwrmgr_base_vseq, so we are moving all functionality to the latter.
    This PR disables that agent and a subsequent one will remove it.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
