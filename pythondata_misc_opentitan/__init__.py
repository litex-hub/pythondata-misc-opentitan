import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11504"
version_tuple = (0, 0, 11504)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11504")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11378"
data_version_tuple = (0, 0, 11378)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11378")
except ImportError:
    pass
data_git_hash = "079a2b8ad742d233b6890ff3b1f32836ab4b8966"
data_git_describe = "v0.0-11378-g079a2b8ad"
data_git_msg = """\
commit 079a2b8ad742d233b6890ff3b1f32836ab4b8966
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Fri Apr 8 14:21:29 2022 +0100

    [otbn, dv] Disables assertions in prim_lc_sync when sending invalid LC signals
    
    This commit turns off assertion failures in prim_lc_sync when invalid
    values are driven on lc_en_i.
    
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
