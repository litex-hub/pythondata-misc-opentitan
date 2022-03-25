import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11136"
version_tuple = (0, 0, 11136)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11136")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11010"
data_version_tuple = (0, 0, 11010)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11010")
except ImportError:
    pass
data_git_hash = "c1f1cb49adca3414562349d86f37264bfbd021c9"
data_git_describe = "v0.0-11010-gc1f1cb49a"
data_git_msg = """\
commit c1f1cb49adca3414562349d86f37264bfbd021c9
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Mar 24 14:02:40 2022 -0700

    [silicon_creator/mask_rom] fix bug in AST init asm
    
    This fixes #11117 by updating the AST init code to actually load the
    correct word at the correct offset in OTP, rather than just loading the
    address itself.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
