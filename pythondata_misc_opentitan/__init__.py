import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9683"
version_tuple = (0, 0, 9683)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9683")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9561"
data_version_tuple = (0, 0, 9561)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9561")
except ImportError:
    pass
data_git_hash = "a06044b38635655c59396463d743b7d5bf9dd287"
data_git_describe = "v0.0-9561-ga06044b38"
data_git_msg = """\
commit a06044b38635655c59396463d743b7d5bf9dd287
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue Jan 18 13:35:36 2022 +0000

    [rom_ctrl, dv] Fixes regression failures in rom_ctrl_passthru_mem_tl_intg_err
    
    Fixes regression failures in rom_ctrl_passthru_mem_tl_intg_err testcase.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
