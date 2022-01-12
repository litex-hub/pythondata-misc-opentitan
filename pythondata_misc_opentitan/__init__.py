import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9455"
version_tuple = (0, 0, 9455)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9455")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9337"
data_version_tuple = (0, 0, 9337)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9337")
except ImportError:
    pass
data_git_hash = "c3bd8451e23db3cc941ec9636735ab592d1c70bb"
data_git_describe = "v0.0-9337-gc3bd8451e"
data_git_msg = """\
commit c3bd8451e23db3cc941ec9636735ab592d1c70bb
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Jan 11 09:55:09 2022 +0100

    [primgen] Update AscentLint waiver in generated abstract prim wrappers
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
