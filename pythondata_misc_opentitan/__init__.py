import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14403"
version_tuple = (0, 0, 14403)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14403")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14261"
data_version_tuple = (0, 0, 14261)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14261")
except ImportError:
    pass
data_git_hash = "0306ab20de0ccc13b6154821f387010613d2c853"
data_git_describe = "v0.0-14261-g0306ab20de"
data_git_msg = """\
commit 0306ab20de0ccc13b6154821f387010613d2c853
Author: Dan McArdle <dmcardle@google.com>
Date:   Fri Sep 23 11:50:38 2022 -0400

    [bazel] Reduce scope of Bazel repo clone for airgapped dir
    
    Prior to this change, we cloned the entire Bazel repo and it took ~40
    seconds on my machine. Cloning only the tag that we want, with a depth
    of 1, brings that down to ~9 seconds, for a total saving of ~31 seconds.
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
