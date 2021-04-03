import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5705"
version_tuple = (0, 0, 5705)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5705")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5610"
data_version_tuple = (0, 0, 5610)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5610")
except ImportError:
    pass
data_git_hash = "2366e55ff0f14ef05445b3251c1dd1c03dd69d6d"
data_git_describe = "v0.0-5610-g2366e55ff"
data_git_msg = """\
commit 2366e55ff0f14ef05445b3251c1dd1c03dd69d6d
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Apr 2 11:34:36 2021 -0700

    [dv/otp] build-in fcov
    
    This PR adds interrupt related build-in fcov. And it updates
    max_outstanding_item to 1, according to design.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
