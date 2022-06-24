import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12844"
version_tuple = (0, 0, 12844)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12844")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12702"
data_version_tuple = (0, 0, 12702)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12702")
except ImportError:
    pass
data_git_hash = "bb30778890d8e030b77ab7dc1a54a471d3a2dc9d"
data_git_describe = "v0.0-12702-gbb30778890"
data_git_msg = """\
commit bb30778890d8e030b77ab7dc1a54a471d3a2dc9d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jun 24 15:08:33 2022 -0700

    [dv/alert_handler] Align crashdump
    
    This PR aligns design change with crashdump feature #13177.
    
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
