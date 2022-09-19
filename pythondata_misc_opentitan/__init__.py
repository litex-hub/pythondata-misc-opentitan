import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14298"
version_tuple = (0, 0, 14298)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14298")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14156"
data_version_tuple = (0, 0, 14156)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14156")
except ImportError:
    pass
data_git_hash = "343e4faf144f69ef4c862e6c86933859cf0a3284"
data_git_describe = "v0.0-14156-g343e4faf14"
data_git_msg = """\
commit 343e4faf144f69ef4c862e6c86933859cf0a3284
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Sat Sep 17 13:19:00 2022 -0700

    [dv/kmac] Force random internal mubi values
    
    This PR adds a sequence for mubi sec countermeasures to make sure when
    forcing mubi value to non-true or non-false, the IP behaves as expected.
    
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
