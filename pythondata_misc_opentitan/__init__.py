import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14666"
version_tuple = (0, 0, 14666)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14666")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14524"
data_version_tuple = (0, 0, 14524)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14524")
except ImportError:
    pass
data_git_hash = "d0b9668b20f6df02bb242a166ae31d1e7c55ad34"
data_git_describe = "v0.0-14524-gd0b9668b20"
data_git_msg = """\
commit d0b9668b20f6df02bb242a166ae31d1e7c55ad34
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Oct 7 17:08:34 2022 -0700

    [fpv] add correct settings for clkmgr
    
    This PR adds clk and reset for clkmgr module.
    
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
