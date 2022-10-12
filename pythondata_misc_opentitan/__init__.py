import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14703"
version_tuple = (0, 0, 14703)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14703")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14561"
data_version_tuple = (0, 0, 14561)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14561")
except ImportError:
    pass
data_git_hash = "c90806027a6d441be74cf66e66c2a585c9f7e383"
data_git_describe = "v0.0-14561-gc90806027a"
data_git_msg = """\
commit c90806027a6d441be74cf66e66c2a585c9f7e383
Author: Chris Frantz <cfrantz@google.com>
Date:   Tue Oct 4 07:14:52 2022 -0700

    [cleanup] Fix `bazelisk outquery` to accept all arguments
    
    `bazelisk.sh outquery` should accept all arguments so that things like
    `--define ...` and `-c opt` are accounted for by the query.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
