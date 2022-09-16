import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14251"
version_tuple = (0, 0, 14251)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14251")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14109"
data_version_tuple = (0, 0, 14109)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14109")
except ImportError:
    pass
data_git_hash = "4cbd30c1a12d66713f42b0be28308ba4014aac98"
data_git_describe = "v0.0-14109-g4cbd30c1a1"
data_git_msg = """\
commit 4cbd30c1a12d66713f42b0be28308ba4014aac98
Author: Eli Kim <eli@opentitan.org>
Date:   Thu Sep 15 16:59:29 2022 -0700

    feat(chip): Add Deep Powerdown Indicator
    
    `pwrmgr_low_power_if.low_power` represents if the chip enters low power
    mode or not. The low power is the moment PWRMGR gating clocks to peri.
    
    Deep powerdown happens after a few additional steps.
    
    This commit uses AST main_pok feeding into pwrmgr as deep powerdown
    indicator.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
