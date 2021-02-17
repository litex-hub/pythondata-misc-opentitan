import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5023"
version_tuple = (0, 0, 5023)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5023")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4932"
data_version_tuple = (0, 0, 4932)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4932")
except ImportError:
    pass
data_git_hash = "81ada4f0c26389e4175e0236eabe1124203d6850"
data_git_describe = "v0.0-4932-g81ada4f0c"
data_git_msg = """\
commit 81ada4f0c26389e4175e0236eabe1124203d6850
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Feb 16 15:59:39 2021 +0000

    [ci] Remove --fork-point from git merge-base command
    
    The --fork-point argument enables a complicated mode for git
    merge-base, which tries to cope with situations where the branch from
    which we forked (origin/master) has had rewrites.
    
    This uses the reflog when searching for ancestors, which isn't
    appropriate in CI (where we're working on fresh checkouts). It seems
    that this fails occasionally, leading to rather mysterious CI errors.
    
    Since we don't rewrite the master branch, just use vanilla merge-base.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
