import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15103"
version_tuple = (0, 0, 15103)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15103")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14961"
data_version_tuple = (0, 0, 14961)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14961")
except ImportError:
    pass
data_git_hash = "eb0bd40a0b48e8c9cb111f2aef4125cda34fd5e8"
data_git_describe = "v0.0-14961-geb0bd40a0b"
data_git_msg = """\
commit eb0bd40a0b48e8c9cb111f2aef4125cda34fd5e8
Author: Miles Dai <milesdai@google.com>
Date:   Tue Nov 1 17:04:10 2022 -0400

    [ci] Enable Vivado on FPGA runners
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
