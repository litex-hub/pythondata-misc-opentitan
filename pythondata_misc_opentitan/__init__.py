import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14913"
version_tuple = (0, 0, 14913)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14913")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14771"
data_version_tuple = (0, 0, 14771)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14771")
except ImportError:
    pass
data_git_hash = "8e158a1578f92239dca253d10834df72b51c132f"
data_git_describe = "v0.0-14771-g8e158a1578"
data_git_msg = """\
commit 8e158a1578f92239dca253d10834df72b51c132f
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Oct 24 10:14:30 2022 -0700

    [dv/chip] Fix unmapped testplan
    
    This PR fixes unmapped testplan in nightly regression.
    
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
