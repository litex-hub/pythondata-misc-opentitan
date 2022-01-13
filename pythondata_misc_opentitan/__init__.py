import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9518"
version_tuple = (0, 0, 9518)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9518")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9396"
data_version_tuple = (0, 0, 9396)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9396")
except ImportError:
    pass
data_git_hash = "b61a21962d180abe6e510db3fd726a5afe6a8b00"
data_git_describe = "v0.0-9396-gb61a21962"
data_git_msg = """\
commit b61a21962d180abe6e510db3fd726a5afe6a8b00
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jan 11 15:51:21 2022 -0800

    [clkmgr] various spec and parameter updates
    
    @matutem pointed out various shortcomings of the existing checks.
    Since these gaps cannot be easily improved, the spec should at least
    clearly explain what the minimal detection resolution is.
    
    - Fixes #8164
    - Fixes #9969
    
    Also shrink the timeout margin to ensure timeout checks are not unnecessarily
    large.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
