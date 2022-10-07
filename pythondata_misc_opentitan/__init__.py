import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14606"
version_tuple = (0, 0, 14606)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14606")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14464"
data_version_tuple = (0, 0, 14464)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14464")
except ImportError:
    pass
data_git_hash = "1bc7ba3536a2240ef209e9acd4b7fed1e32cac91"
data_git_describe = "v0.0-14464-g1bc7ba3536"
data_git_msg = """\
commit 1bc7ba3536a2240ef209e9acd4b7fed1e32cac91
Author: Eli Kim <eli@opentitan.org>
Date:   Thu Oct 6 11:24:37 2022 -0700

    feat(chip): Scaffolds SV test env for sleep_pin_retention
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
