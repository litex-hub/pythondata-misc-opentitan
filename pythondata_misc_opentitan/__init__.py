import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14540"
version_tuple = (0, 0, 14540)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14540")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14398"
data_version_tuple = (0, 0, 14398)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14398")
except ImportError:
    pass
data_git_hash = "81b7f4049e18a077da549f860beeb201d0471bd2"
data_git_describe = "v0.0-14398-g81b7f4049e"
data_git_msg = """\
commit 81b7f4049e18a077da549f860beeb201d0471bd2
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Oct 3 15:42:14 2022 -0700

    [dv/kmac] Change kmac_fsm to terminal error to base exclusion file
    
    This PR changes the masked version of the kmac state to terminal error
    state exclusion file to a base exclusion file.
    Because both the masked and unmasked versions share the same exclusion
    items.
    
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
