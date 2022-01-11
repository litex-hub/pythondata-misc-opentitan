import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9425"
version_tuple = (0, 0, 9425)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9425")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9307"
data_version_tuple = (0, 0, 9307)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9307")
except ImportError:
    pass
data_git_hash = "a894cec40a0fe19ecce2bbbf3d06699f074a8d9b"
data_git_describe = "v0.0-9307-ga894cec40"
data_git_msg = """\
commit a894cec40a0fe19ecce2bbbf3d06699f074a8d9b
Author: Luís Marques <luismarques@lowrisc.org>
Date:   Fri Jan 7 00:35:13 2022 +0000

    [sw, host] Update Mundane version
    
    This updates the dependency Mundane to version 0.5.0. That version includes
    the latest BoringSSL version, which fixes compilation errors with recent
    versions of GCC.
    
    Signed-off-by: Luís Marques <luismarques@lowrisc.org>

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
