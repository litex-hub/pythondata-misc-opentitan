import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12524"
version_tuple = (0, 0, 12524)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12524")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12382"
data_version_tuple = (0, 0, 12382)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12382")
except ImportError:
    pass
data_git_hash = "1bd62be4b9fb64e6e7f314ebe081da0202d0bd6e"
data_git_describe = "v0.0-12382-g1bd62be4b"
data_git_msg = """\
commit 1bd62be4b9fb64e6e7f314ebe081da0202d0bd6e
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Jun 1 10:32:14 2022 +0100

    [otbn, rtl] Add prim_buf and prim_flop
    
    These add needed optimization barriers around security hardening
    features.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
