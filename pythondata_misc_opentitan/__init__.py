import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12950"
version_tuple = (0, 0, 12950)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12950")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12808"
data_version_tuple = (0, 0, 12808)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12808")
except ImportError:
    pass
data_git_hash = "aa110dcac555bcb3287a95ff9108451a80b2d6e7"
data_git_describe = "v0.0-12808-gaa110dcac5"
data_git_msg = """\
commit aa110dcac555bcb3287a95ff9108451a80b2d6e7
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Jul 6 11:51:21 2022 -0700

    [dv/alert_handler] Update alert_handler output timing
    
    This PR updates alert_handler test timeout timing.
    
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
