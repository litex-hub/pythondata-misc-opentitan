import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15078"
version_tuple = (0, 0, 15078)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15078")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14936"
data_version_tuple = (0, 0, 14936)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14936")
except ImportError:
    pass
data_git_hash = "3ad51c3b4fa9a10c865d9e9ea0b6b87266ebd392"
data_git_describe = "v0.0-14936-g3ad51c3b4f"
data_git_msg = """\
commit 3ad51c3b4fa9a10c865d9e9ea0b6b87266ebd392
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Oct 31 11:30:10 2022 -0700

    [edn] Tweak fifo clear logic
    
    - Currently, the generate and reseed command fifos can only be
      cleared when edn is enabled. This means when software disables
      the edn to reset it into a different mode (boot to auto for
      example), it has to actually wait until edn is re-enabled to
      clear the FIFOs.  This can lead to some odd corner cases where
      the edn / csrng interface can actually get stuck because a
      previous command accidentally goes through.
    
    - To get around this, allow the reseed / generate command fifos
      to be cleared regardless of the edn enable state.
    
    - This fixes #14506
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
