import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14769"
version_tuple = (0, 0, 14769)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14769")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14627"
data_version_tuple = (0, 0, 14627)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14627")
except ImportError:
    pass
data_git_hash = "7aa862374f40d29ec7dd2029b20aec650c1f79b0"
data_git_describe = "v0.0-14627-g7aa862374f"
data_git_msg = """\
commit 7aa862374f40d29ec7dd2029b20aec650c1f79b0
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Thu Oct 13 19:46:38 2022 -0700

    [entropy_src/dv] Close sw_update_cg
    
    This commit updates the RNG test, dut_cfg structure and RNG vseq to close the
    sw_update_cg.  This includes:
    
    - Adding randomized config variables to _not_ disable the DUT before
      reconfiguration
    - Randomizing the sw_regupd field
    - Forcing the DUT into the enabled state when the disabled state is not
      requested.
    - Forcing an _unlocked_ reconfiguration (and if needed a reset) once a
      locked reconfiguration has been attempted.
    - Only sampling coverage when a new attempted setting is different
      from the current setting (and thus any lock errors are detectable).
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
