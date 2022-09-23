import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14397"
version_tuple = (0, 0, 14397)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14397")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14255"
data_version_tuple = (0, 0, 14255)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14255")
except ImportError:
    pass
data_git_hash = "b72304ab6bc403b819e54329ee8e153c6438f4e6"
data_git_describe = "v0.0-14255-gb72304ab6b"
data_git_msg = """\
commit b72304ab6bc403b819e54329ee8e153c6438f4e6
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Sep 15 15:21:42 2022 +0100

    [otbn,fcov] Add RND spurious ack error coverpoint
    
    In the comment linked below, a spurious ack check feature said to
    include RND as well as URND. This commit extends bad_internal_cg to
    include that error as well.
    
    https://github.com/lowRISC/opentitan/issues/11546#issuecomment-1172031776
    
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
