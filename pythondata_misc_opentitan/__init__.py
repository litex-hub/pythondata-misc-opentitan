import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12578"
version_tuple = (0, 0, 12578)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12578")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12436"
data_version_tuple = (0, 0, 12436)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12436")
except ImportError:
    pass
data_git_hash = "f7337a3404400ba3af289813f28653e11ce9ccfb"
data_git_describe = "v0.0-12436-gf7337a340"
data_git_msg = """\
commit f7337a3404400ba3af289813f28653e11ce9ccfb
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Jun 8 14:31:44 2022 -0700

    [dv/kmac] Fix escalation regression failure
    
    This PR fixes KMAC lc_escalation test failure in nightly regression.
    The main issue is that now that lc_escalation triggers a fatal alert and
    also interrupt. So before reset, the interrupt will continously fire.
    To avoid this issue, I moved the interrupt checking after fatal alert
    stops firing. Also fixes an issue that the test does not revert back
    lc_escalation_en signal.
    
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
