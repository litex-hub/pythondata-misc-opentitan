import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12729"
version_tuple = (0, 0, 12729)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12729")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12587"
data_version_tuple = (0, 0, 12587)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12587")
except ImportError:
    pass
data_git_hash = "87fc75187ad2a01b2e972ff7eb125cafadeaedde"
data_git_describe = "v0.0-12587-g87fc75187"
data_git_msg = """\
commit 87fc75187ad2a01b2e972ff7eb125cafadeaedde
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Jun 16 17:32:55 2022 +0100

    [otbn, rtl] Clarify multiple base RF WEs in predecoder
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
