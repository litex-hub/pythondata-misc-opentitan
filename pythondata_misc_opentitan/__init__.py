import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8216"
version_tuple = (0, 0, 8216)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8216")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8104"
data_version_tuple = (0, 0, 8104)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8104")
except ImportError:
    pass
data_git_hash = "f139f833c0feeec10c053ec53510aca6137a5232"
data_git_describe = "v0.0-8104-gf139f833c"
data_git_msg = """\
commit f139f833c0feeec10c053ec53510aca6137a5232
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Oct 11 18:05:26 2021 +0100

    [otbn,dv] Weaken a compatibility check between stall and exec lines
    
    This is needed to handle the trace output that you get if you inject
    an IMEM error while an instruction is stalled.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
