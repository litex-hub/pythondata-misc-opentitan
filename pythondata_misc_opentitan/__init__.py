import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8875"
version_tuple = (0, 0, 8875)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8875")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8763"
data_version_tuple = (0, 0, 8763)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8763")
except ImportError:
    pass
data_git_hash = "ffb02b25462524ee90a9587844c4610e7e4ec32a"
data_git_describe = "v0.0-8763-gffb02b254"
data_git_msg = """\
commit ffb02b25462524ee90a9587844c4610e7e4ec32a
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Nov 25 14:00:30 2021 +0100

    [aes, pre_sca] Enable formal verification of more than a single S-Box
    
    This commit enables the formal verification of either the full SubBytes,
    i.e., the 16 S-Boxes in the data path, and even a reduced AES round
    containing also ShiftRows and MixColumns. This is useful as formal
    verification of the entire AES cipher core is currently out of scope
    from a tool run time point of view whereas SCA leakage outside the
    reduced AES round is unlikely.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
