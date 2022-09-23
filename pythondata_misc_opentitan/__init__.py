import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14405"
version_tuple = (0, 0, 14405)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14405")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14263"
data_version_tuple = (0, 0, 14263)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14263")
except ImportError:
    pass
data_git_hash = "45c4af7f7897731fed233e17500a888b97b8bc98"
data_git_describe = "v0.0-14263-g45c4af7f78"
data_git_msg = """\
commit 45c4af7f7897731fed233e17500a888b97b8bc98
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Sep 23 08:57:19 2022 -0700

    [dv/shadow_reg] Update comment
    
    This PR updates a comment in shadow reg RAL prediction.
    The comment mentioned the update condition is during the update error,
    which is incorrect.
    
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
