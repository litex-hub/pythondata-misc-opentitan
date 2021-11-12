import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8695"
version_tuple = (0, 0, 8695)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8695")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8583"
data_version_tuple = (0, 0, 8583)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8583")
except ImportError:
    pass
data_git_hash = "dd3a05bc5abc9dd2874896f171d12c6eaf1576f3"
data_git_describe = "v0.0-8583-gdd3a05bc5"
data_git_msg = """\
commit dd3a05bc5abc9dd2874896f171d12c6eaf1576f3
Author: Vladimir Rozic <vrozic@lowrisc.org>
Date:   Thu Nov 11 12:11:46 2021 +0000

    [otbn] Updated uRNG in OTBN
    
    Replaced OTBN's LFSR-based PRNG with xoshiro256pp.
    
    Signed-off-by: Vladimir Rozic <vrozic@lowrisc.org>

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
