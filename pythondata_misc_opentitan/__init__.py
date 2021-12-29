import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9301"
version_tuple = (0, 0, 9301)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9301")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9184"
data_version_tuple = (0, 0, 9184)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9184")
except ImportError:
    pass
data_git_hash = "5711ee677dc28fc19894060c320df82a2ea6c381"
data_git_describe = "v0.0-9184-g5711ee677"
data_git_msg = """\
commit 5711ee677dc28fc19894060c320df82a2ea6c381
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Dec 28 12:09:46 2021 -0800

    [fpv/pinmux] Update jtag pinmux assertion
    
    This PR adds assertions on jtag ports in pinmux based on internal
    variable `tap_strap`.
    Next PR will write assertions to ensure `tap_strap` is correct.
    
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
