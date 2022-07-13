import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13067"
version_tuple = (0, 0, 13067)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13067")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12925"
data_version_tuple = (0, 0, 12925)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12925")
except ImportError:
    pass
data_git_hash = "f353489e0d9a9645eeb4e07c3766640e20798af8"
data_git_describe = "v0.0-12925-gf353489e0d"
data_git_msg = """\
commit f353489e0d9a9645eeb4e07c3766640e20798af8
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Jul 13 12:19:52 2022 -0700

    [chip/conn] Move a DV testplan entry to connectivity testplan
    
    This PR removes a DV testplan entry (EDN clock and reset check in OTP)
    to a connectivity check. We discussed this topic in one of the DV
    meeting and found that there aren't any check points in simulation due
    to the clock and reset groups. So we move this to a connectivity check.
    
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
