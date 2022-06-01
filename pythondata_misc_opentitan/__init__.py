import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12431"
version_tuple = (0, 0, 12431)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12431")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12289"
data_version_tuple = (0, 0, 12289)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12289")
except ImportError:
    pass
data_git_hash = "e9cfd0f0f3de2b58fe472d5bcb8ad4a0a6e4e88a"
data_git_describe = "v0.0-12289-ge9cfd0f0f"
data_git_msg = """\
commit e9cfd0f0f3de2b58fe472d5bcb8ad4a0a6e4e88a
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu May 26 10:54:34 2022 +0100

    [otbn,rtl] Refactor ISPR read muxing
    
    ISPR read data is muxed out in two stages in the bignum ALU. The first
    stage muxes between all of the ISPRs that don't have integrity bits. The
    result goes through an integrity encoder and is fed into the second
    stage. The second stage chooses the final read data choosing between the
    first stage with the calculated intergrity and the ISPRs that have
    integrity bits.
    
    This refactoring makes this structure more explicit and should result in
    area savings as the previous RTL fed the same signal into multiple
    inputs of the second stage mux. As there is an optimization barrier in
    the mux these would not have been optimized down to a single input.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
