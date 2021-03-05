import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5251"
version_tuple = (0, 0, 5251)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5251")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5160"
data_version_tuple = (0, 0, 5160)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5160")
except ImportError:
    pass
data_git_hash = "aec65bab197ed9578f36a27ec5dcd2298801686e"
data_git_describe = "v0.0-5160-gaec65bab1"
data_git_msg = """\
commit aec65bab197ed9578f36a27ec5dcd2298801686e
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Wed Feb 24 16:36:55 2021 +0000

    [sw, dif_pinmux] Introduce DIF Pinmux header
    
    Please note that this is a reworked version of the following PRs:
    https://github.com/lowRISC/opentitan/pull/2042 (PadCtrl)
    https://github.com/lowRISC/opentitan/pull/1763 (Pinmux)
    
    This is due to major changes in hardware - PadCtrl and Pinmux have
    been merged into one (Pinmux).
    
    Please note that all of the PadCtrl functionality was written by Greg
    Chadwick, and was copied into this change with some minor naming
    changes.
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
