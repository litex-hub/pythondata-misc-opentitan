import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14511"
version_tuple = (0, 0, 14511)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14511")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14369"
data_version_tuple = (0, 0, 14369)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14369")
except ImportError:
    pass
data_git_hash = "54a68b0b1d680a3ef8853626db2880999b87aa7a"
data_git_describe = "v0.0-14369-g54a68b0b1d"
data_git_msg = """\
commit 54a68b0b1d680a3ef8853626db2880999b87aa7a
Author: Eli Kim <eli@opentitan.org>
Date:   Wed Sep 28 15:10:04 2022 -0700

    fix(rdc): SPID CSb, TPM CSb waiver for COMBO
    
    Waiving SPI_DEVICE CS#, TPM CS# reset signal sitting on COMBO logic. The
    logic OR-ed with scan chain.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
