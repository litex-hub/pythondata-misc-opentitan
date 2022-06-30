import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12904"
version_tuple = (0, 0, 12904)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12904")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12762"
data_version_tuple = (0, 0, 12762)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12762")
except ImportError:
    pass
data_git_hash = "236eaf3da5c596ee891410f7ac4a2e22d848c564"
data_git_describe = "v0.0-12762-g236eaf3da5"
data_git_msg = """\
commit 236eaf3da5c596ee891410f7ac4a2e22d848c564
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Jun 27 16:07:10 2022 -0700

    [dv,chip,power_glitch] Fix deep_sleep power glitch test
    
    Trigger the glitch when pwrmgr has just set reset_cause to LowPwrEntry.
    If the trigger event happens with more relaxed timing the results are
    unpredictable: either reset happens before low power entry, or pwrmgr
    could have stopped monitoring power glitches.
    
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
