import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5010"
version_tuple = (0, 0, 5010)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5010")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4919"
data_version_tuple = (0, 0, 4919)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4919")
except ImportError:
    pass
data_git_hash = "a5973fbc32af0b21cb2a00e3acc293642b4ae097"
data_git_describe = "v0.0-4919-ga5973fbc3"
data_git_msg = """\
commit a5973fbc32af0b21cb2a00e3acc293642b4ae097
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Feb 16 13:16:11 2021 +0100

    [fpga] Fix clock constraints
    
    The clkmgr instance got renamed recently. As a result, the clock
    constraints couldn't be applied, leaving many clocks unconstrained on FPGA.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
