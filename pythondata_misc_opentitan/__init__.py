import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11513"
version_tuple = (0, 0, 11513)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11513")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11387"
data_version_tuple = (0, 0, 11387)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11387")
except ImportError:
    pass
data_git_hash = "5fd9acdb61b2eb0d6ecce5037e33d4d59850c3dd"
data_git_describe = "v0.0-11387-g5fd9acdb6"
data_git_msg = """\
commit 5fd9acdb61b2eb0d6ecce5037e33d4d59850c3dd
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Apr 8 18:48:23 2022 +0000

    pwrmgr,dv] v2s_review_ready
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
