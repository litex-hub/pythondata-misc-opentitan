import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8481"
version_tuple = (0, 0, 8481)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8481")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8369"
data_version_tuple = (0, 0, 8369)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8369")
except ImportError:
    pass
data_git_hash = "0836ef34d6ab6912702683d68fe2c81cc147ade2"
data_git_describe = "v0.0-8369-g0836ef34d"
data_git_msg = """\
commit 0836ef34d6ab6912702683d68fe2c81cc147ade2
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Oct 26 17:14:54 2021 -0700

    [doc/sw] Add specific example to build documentation
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
