import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13119"
version_tuple = (0, 0, 13119)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13119")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12977"
data_version_tuple = (0, 0, 12977)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12977")
except ImportError:
    pass
data_git_hash = "0962269c706650526c858a3522100c0364a75c6b"
data_git_describe = "v0.0-12977-g0962269c70"
data_git_msg = """\
commit 0962269c706650526c858a3522100c0364a75c6b
Author: Joshua Park <jeoong@google.com>
Date:   Wed Jun 29 17:28:33 2022 -0700

    [cdc] misc. waivers
    
    AST clocks : waived S_GENCLK errors
    SPI_DEVICE :
    - Black-boxing dual port SRAM
    - Waived paths from TLUL error to u_reg
    
    Signed-off-by: Joshua Park <jeoong@google.com>

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
