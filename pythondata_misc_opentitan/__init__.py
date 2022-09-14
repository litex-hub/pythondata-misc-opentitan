import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14186"
version_tuple = (0, 0, 14186)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14186")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14044"
data_version_tuple = (0, 0, 14044)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14044")
except ImportError:
    pass
data_git_hash = "94e1ca7da17dd6ff39e7ab34e4f6a7b0f27b3b74"
data_git_describe = "v0.0-14044-g94e1ca7da1"
data_git_msg = """\
commit 94e1ca7da17dd6ff39e7ab34e4f6a7b0f27b3b74
Author: Jade Philipoom <jadep@google.com>
Date:   Thu Sep 1 14:36:10 2022 +0200

    [crypto] Remove now-empty header file.
    
    Final step in splitting api.h into many header files; remove the
    now-empty api.h.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
