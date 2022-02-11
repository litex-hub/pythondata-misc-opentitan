import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10243"
version_tuple = (0, 0, 10243)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10243")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10119"
data_version_tuple = (0, 0, 10119)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10119")
except ImportError:
    pass
data_git_hash = "4360bf23629d1d5771f0340b6d4772ebdd1f6f5a"
data_git_describe = "v0.0-10119-g4360bf236"
data_git_msg = """\
commit 4360bf23629d1d5771f0340b6d4772ebdd1f6f5a
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Feb 9 16:12:43 2022 -0800

    [clkmgr] Add secure buffers for clkmgr byp_req
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
