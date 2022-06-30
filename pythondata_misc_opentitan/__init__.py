import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12898"
version_tuple = (0, 0, 12898)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12898")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12756"
data_version_tuple = (0, 0, 12756)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12756")
except ImportError:
    pass
data_git_hash = "9c280944cd69aa74e2b98c0d572e232582bcbf87"
data_git_describe = "v0.0-12756-g9c280944cd"
data_git_msg = """\
commit 9c280944cd69aa74e2b98c0d572e232582bcbf87
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jun 30 08:36:56 2022 -0700

    [dv/alert_handler] Enhance EDN timing check
    
    The spec specifies that EDN request should be refreshed every 500k clock
    cycles.
    This PR:
    1). Adds a checking in scb to make sure this timing requirement is
      satisfied.
    2). Add functional coverage group to make sure we run simulation long
      enough to capture EDN requests at least 5 times.
    
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
