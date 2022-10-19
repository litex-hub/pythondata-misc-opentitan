import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14812"
version_tuple = (0, 0, 14812)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14812")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14670"
data_version_tuple = (0, 0, 14670)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14670")
except ImportError:
    pass
data_git_hash = "faa6cab3d58a88ad18905223d4a74a2c4f94c9fa"
data_git_describe = "v0.0-14670-gfaa6cab3d5"
data_git_msg = """\
commit faa6cab3d58a88ad18905223d4a74a2c4f94c9fa
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Mon Oct 17 21:34:46 2022 -0700

    [entropy_src/dv] Temporarily exclude Extht related regs/ports
    
    This commit adds a new vRefine file to waive coverge on ports related
    to the ExtHT ports. The ExtHT agent (and supported vseq updates) should
    be able to close these coverage points, but this is not a priority for
    now.  So we should waive them for the time being.
    
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
