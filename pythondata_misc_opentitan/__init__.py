import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12882"
version_tuple = (0, 0, 12882)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12882")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12740"
data_version_tuple = (0, 0, 12740)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12740")
except ImportError:
    pass
data_git_hash = "a96565ddbe684f14663c187db8a6c17908eebfbc"
data_git_describe = "v0.0-12740-ga96565ddbe"
data_git_msg = """\
commit a96565ddbe684f14663c187db8a6c17908eebfbc
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jun 28 15:07:04 2022 -0700

    [alert_handler/fpv] Fix local_alert index in regen error
    
    This PR fixes the alert_handler_sec_cm failure where we expect to see
    loc_alert[2] to fire when regen failed. But from the spec, loc_alert[2]
    is alert integfail but loc_alert[4] is for bus integrity failure.
    So this PR fixes this typo.
    
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
