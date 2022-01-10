import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9409"
version_tuple = (0, 0, 9409)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9409")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9291"
data_version_tuple = (0, 0, 9291)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9291")
except ImportError:
    pass
data_git_hash = "f97c020377051ee4816f152f235a195093555775"
data_git_describe = "v0.0-9291-gf97c02037"
data_git_msg = """\
commit f97c020377051ee4816f152f235a195093555775
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Thu Jan 6 17:37:42 2022 +0000

    [rom_ctrl, dv] Added passthru mem test
    
    Added all the necessary changes to include
    rom_ctrl_passthru_mem_tl_intg_err for rom controller module
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
