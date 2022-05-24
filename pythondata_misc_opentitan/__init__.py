import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12301"
version_tuple = (0, 0, 12301)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12301")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12173"
data_version_tuple = (0, 0, 12173)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12173")
except ImportError:
    pass
data_git_hash = "d9a7c02c1880cc5c8c58f0d51c65003ee3152551"
data_git_describe = "v0.0-12173-gd9a7c02c1"
data_git_msg = """\
commit d9a7c02c1880cc5c8c58f0d51c65003ee3152551
Author: Jon Flatley <jflat@google.com>
Date:   Tue May 24 10:44:29 2022 -0400

    [opentitanlib] Fix manifest HJSON deserialization
    
    Manifest deserialization is failing on HJSON files with missing fields.
    Add the #[serde(default)] attribute to manifest fields to fix this.
    
    Signed-off-by: Jon Flatley <jflat@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
