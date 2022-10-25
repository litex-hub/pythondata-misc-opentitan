import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14937"
version_tuple = (0, 0, 14937)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14937")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14795"
data_version_tuple = (0, 0, 14795)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14795")
except ImportError:
    pass
data_git_hash = "b001ebce67385ae7fa47649d792b9361362ee6b6"
data_git_describe = "v0.0-14795-gb001ebce67"
data_git_msg = """\
commit b001ebce67385ae7fa47649d792b9361362ee6b6
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Oct 24 16:51:12 2022 -0700

    [fpv/pinmux] Fix pinmux compile error
    
    This PR fixes pinmux compile error due to the intg_error hierarchy
    change.
    
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
