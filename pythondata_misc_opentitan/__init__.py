import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12678"
version_tuple = (0, 0, 12678)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12678")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12536"
data_version_tuple = (0, 0, 12536)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12536")
except ImportError:
    pass
data_git_hash = "46dc8f7d6c5638b5705cc3f7a098796c5939ec81"
data_git_describe = "v0.0-12536-g46dc8f7d6"
data_git_msg = """\
commit 46dc8f7d6c5638b5705cc3f7a098796c5939ec81
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Jun 14 11:28:48 2022 -0400

    [sw/silicon_creator] Preserve upper bits of the cpuctrl CSR
    
    This commit updates the way cpuctrl CSR is written in mask_rom_init()
    such that its upper bits, more specifically `double_fault_seen` (bit 6)
    and `double_fault_seen` (bit 7), are preserved.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
