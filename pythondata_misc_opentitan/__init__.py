import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10347"
version_tuple = (0, 0, 10347)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10347")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10221"
data_version_tuple = (0, 0, 10221)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10221")
except ImportError:
    pass
data_git_hash = "a79607b660924d016e70ffe8893a30c91e15c91c"
data_git_describe = "v0.0-10221-ga79607b66"
data_git_msg = """\
commit a79607b660924d016e70ffe8893a30c91e15c91c
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Mon Jan 24 11:30:09 2022 +0000

    [rom_ctrl, dv] Checklist edited to reflect V2 status
    
    All the AIs from V2 review meeting have been completed and hence V2 targets are reached.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
