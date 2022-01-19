import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9636"
version_tuple = (0, 0, 9636)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9636")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9514"
data_version_tuple = (0, 0, 9514)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9514")
except ImportError:
    pass
data_git_hash = "7f09574c615a1540174899148b355837092b9c04"
data_git_describe = "v0.0-9514-g7f09574c6"
data_git_msg = """\
commit 7f09574c615a1540174899148b355837092b9c04
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jan 18 15:44:07 2022 -0800

    [otp_ctrl] Anchor seeds and key output
    
    - Partially address #8983
    - Adds anchor buffers and flops to otp seeds, constants, scramble keys
      and derived keys
    
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
