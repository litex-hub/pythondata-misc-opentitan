import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14398"
version_tuple = (0, 0, 14398)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14398")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14256"
data_version_tuple = (0, 0, 14256)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14256")
except ImportError:
    pass
data_git_hash = "3506890bb969b33e336f367c54c592d32413bb8c"
data_git_describe = "v0.0-14256-g3506890bb9"
data_git_msg = """\
commit 3506890bb969b33e336f367c54c592d32413bb8c
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Sep 15 13:11:00 2022 +0100

    [otbn,dv] Add assertions to check I/DMEM SEC_WIPE
    
    Added assertions are making sure that two things happen. First, a
    secure wipe would trigger a change of key value in I/DMEM in which
    the new value should come from URND. Second, after that change key
    should change a second time, this time with valid being high and
    value should come from OTP interface (meaning it is sideloaded).
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
