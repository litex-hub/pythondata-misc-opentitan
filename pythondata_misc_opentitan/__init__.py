import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9377"
version_tuple = (0, 0, 9377)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9377")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9260"
data_version_tuple = (0, 0, 9260)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9260")
except ImportError:
    pass
data_git_hash = "6e5dec042bd61fa5ff5da3acbb30041e7686e62f"
data_git_describe = "v0.0-9260-g6e5dec042"
data_git_msg = """\
commit 6e5dec042bd61fa5ff5da3acbb30041e7686e62f
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jan 6 17:12:11 2022 -0800

    [dv/top_level] Update top-level kmac testplan
    
    As the email discussion with David, Michael, and Weicai.
    This PR updates top-level kmac testplan related to `entropy_timer`.
    This is replaced by EDN and `entropy_refresh` registers.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
