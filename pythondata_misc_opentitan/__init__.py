import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13188"
version_tuple = (0, 0, 13188)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13188")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13046"
data_version_tuple = (0, 0, 13046)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13046")
except ImportError:
    pass
data_git_hash = "9d0130e0fb42c2dceaf65257d91aa88a300a09b8"
data_git_describe = "v0.0-13046-g9d0130e0fb"
data_git_msg = """\
commit 9d0130e0fb42c2dceaf65257d91aa88a300a09b8
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Wed Jul 20 01:28:57 2022 -0700

    [entropy_src/dv] Temporarily disable some stressors
    
    THe entropy_src_rng sequence is currenly hanging dues to frequent
    fatal errors and an unreliable reset sequence.   This commit
    disables the events causing these fatal errors until the reset
    mechanism can be made more robust.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
