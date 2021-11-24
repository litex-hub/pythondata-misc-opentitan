import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8855"
version_tuple = (0, 0, 8855)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8855")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8743"
data_version_tuple = (0, 0, 8743)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8743")
except ImportError:
    pass
data_git_hash = "78fa36721e3dc9e46ec8836dc55d938306117979"
data_git_describe = "v0.0-8743-g78fa36721"
data_git_msg = """\
commit 78fa36721e3dc9e46ec8836dc55d938306117979
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Nov 19 20:33:38 2021 +0000

    [sw/test_rom] Skip SRAM request for new key and LFSR init in test ROM.
    
    The test `boot_rom` initialization code was requesting and new SRAM
    scrambing key and re-initializing SRAM to pseudorandom values in the
    ROM init asm. This wastes sim cycles as this is not production mask ROM,
    and is used solely for testing.
    
    This commit removes this extra initialization, addressing a task in #9163.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
