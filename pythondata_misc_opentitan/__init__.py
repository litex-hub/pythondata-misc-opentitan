import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10089"
version_tuple = (0, 0, 10089)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10089")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9965"
data_version_tuple = (0, 0, 9965)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9965")
except ImportError:
    pass
data_git_hash = "b4f912be80644aa817f8c10937b60fc7a20b729d"
data_git_describe = "v0.0-9965-gb4f912be8"
data_git_msg = """\
commit b4f912be80644aa817f8c10937b60fc7a20b729d
Author: Weicai Yang <weicai@google.com>
Date:   Thu Feb 3 13:58:50 2022 -0800

    [dv] Fix 2 coverage holes
    
    1. Fixed wrong conditon for enabling byte access error
    2. Fixed never issuing byte write to memory for integrity error
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
