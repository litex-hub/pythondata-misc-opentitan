import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8373"
version_tuple = (0, 0, 8373)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8373")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8261"
data_version_tuple = (0, 0, 8261)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8261")
except ImportError:
    pass
data_git_hash = "37c78bd29b25851f78178d632e078d6ee4ae9d15"
data_git_describe = "v0.0-8261-g37c78bd29"
data_git_msg = """\
commit 37c78bd29b25851f78178d632e078d6ee4ae9d15
Author: Vladimir Rozic <vrozic@lowrisc.org>
Date:   Mon Oct 4 13:17:49 2021 +0100

    [otbn] Added RTL for internal secure wipe
    
    At the end of the OTBN operation the internal state is wiped by
    randomizing (using URNG data) and zeroing:
      -Wide Data registers
      -General purpose registers
      -The accumulator register
      -The modulus
    
    Call and loop stack pointers are reset.
    Flags are set to zero.
    
    This operation can be switched on/off via parameter SecWipeEn
    at otbn_core.sv (default SecWipeEn = 1'b0)
    
    Added internal secure wipe.
    
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
