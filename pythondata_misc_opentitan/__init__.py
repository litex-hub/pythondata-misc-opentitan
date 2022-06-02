import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12462"
version_tuple = (0, 0, 12462)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12462")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12320"
data_version_tuple = (0, 0, 12320)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12320")
except ImportError:
    pass
data_git_hash = "f0e8fd418b5743a2906fde6a07f591bb16da01a7"
data_git_describe = "v0.0-12320-gf0e8fd418"
data_git_msg = """\
commit f0e8fd418b5743a2906fde6a07f591bb16da01a7
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Jun 1 15:19:41 2022 -0400

    [sw/silicon_creator] Use sram_ctrl DIFs in mask_rom_epmp_test.c
    
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
