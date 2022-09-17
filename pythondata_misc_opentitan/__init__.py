import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14283"
version_tuple = (0, 0, 14283)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14283")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14141"
data_version_tuple = (0, 0, 14141)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14141")
except ImportError:
    pass
data_git_hash = "d430668982f70873d7e58245de31da4ed3de51b1"
data_git_describe = "v0.0-14141-gd430668982"
data_git_msg = """\
commit d430668982f70873d7e58245de31da4ed3de51b1
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Sep 13 17:53:44 2022 -0400

    [bazel] Add update_usr_access parameter to bitstream_splice
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
