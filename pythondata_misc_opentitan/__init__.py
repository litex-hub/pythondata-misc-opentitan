import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9414"
version_tuple = (0, 0, 9414)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9414")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9296"
data_version_tuple = (0, 0, 9296)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9296")
except ImportError:
    pass
data_git_hash = "241d606a8a9e1e274c0dcad2ad390d1c28721cf3"
data_git_describe = "v0.0-9296-g241d606a8"
data_git_msg = """\
commit 241d606a8a9e1e274c0dcad2ad390d1c28721cf3
Author: Weicai Yang <weicai@google.com>
Date:   Mon Jan 10 14:06:36 2022 -0800

    [sram/dv] Minor DV doc update
    
    1. added prim_prince, prim_lfsr are verified separately
    2. added using different INSTR_EXEC parameter for ret and main sram
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
