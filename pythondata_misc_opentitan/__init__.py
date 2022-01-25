import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9786"
version_tuple = (0, 0, 9786)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9786")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9664"
data_version_tuple = (0, 0, 9664)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9664")
except ImportError:
    pass
data_git_hash = "9384c5541e47376fa156d234c3aa4b46ef4acb9c"
data_git_describe = "v0.0-9664-g9384c5541"
data_git_msg = """\
commit 9384c5541e47376fa156d234c3aa4b46ef4acb9c
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Jan 25 10:23:19 2022 -0500

    [sw/silicon_creator] Update HARDENED_CHECK comment
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
