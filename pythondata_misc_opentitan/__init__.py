import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14903"
version_tuple = (0, 0, 14903)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14903")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14761"
data_version_tuple = (0, 0, 14761)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14761")
except ImportError:
    pass
data_git_hash = "23dc40e81e83aa575650d76bccf6d53959278dcb"
data_git_describe = "v0.0-14761-g23dc40e81e"
data_git_msg = """\
commit 23dc40e81e83aa575650d76bccf6d53959278dcb
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Oct 21 10:46:17 2022 +0200

    [top] Enable SecAesAllowForcingMasks parameter for top_earlgrey ES
    
    It has been decided to enable this feature for ES. For reference,
    see lowRISC/OpenTitan#14240.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
