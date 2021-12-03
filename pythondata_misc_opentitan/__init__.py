import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8981"
version_tuple = (0, 0, 8981)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8981")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8869"
data_version_tuple = (0, 0, 8869)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8869")
except ImportError:
    pass
data_git_hash = "d5c2d7f97e302b9341587da70483f66bfe41cec2"
data_git_describe = "v0.0-8869-gd5c2d7f97"
data_git_msg = """\
commit d5c2d7f97e302b9341587da70483f66bfe41cec2
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Dec 2 17:10:00 2021 -0800

    [edn / csrng / entropy_src] swap to dv streamlined sparse_fsm
    
    - no functional changes
    - part of #9447 for these blocks
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
