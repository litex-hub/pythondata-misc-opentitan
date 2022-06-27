import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12854"
version_tuple = (0, 0, 12854)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12854")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12712"
data_version_tuple = (0, 0, 12712)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12712")
except ImportError:
    pass
data_git_hash = "cccffd8addcf31bba67d3b8252ec7df94776675f"
data_git_describe = "v0.0-12712-gcccffd8add"
data_git_msg = """\
commit cccffd8addcf31bba67d3b8252ec7df94776675f
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jun 21 22:23:54 2022 -0700

    [dv/otp] Update prim_tl agent
    
    As design supports alias register in open/close source for tl_prim_i/o,
    in open source DV, we switch to use this tl_prim_i/o agent.
    
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
