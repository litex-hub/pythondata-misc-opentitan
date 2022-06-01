import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12449"
version_tuple = (0, 0, 12449)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12449")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12307"
data_version_tuple = (0, 0, 12307)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12307")
except ImportError:
    pass
data_git_hash = "76232bcde543baae1fdf61847c5b508ca31340f5"
data_git_describe = "v0.0-12307-g76232bcde"
data_git_msg = """\
commit 76232bcde543baae1fdf61847c5b508ca31340f5
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Jun 1 17:13:52 2022 +0200

    [otp_ctrl] Temporarily exclude prim CSRs from automatic CSR checks
    
    Since chip-level sims currently do not yet support reading in the alias
    files, we get currently get some mismatches in the chip CSR checks on the
    foundry side due to differing reset values in the prim CSRs.
    
    This patch therefore temporarily adds exclusions for these checks.
    It will be removed once alias files are supported in chip-level sims.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
