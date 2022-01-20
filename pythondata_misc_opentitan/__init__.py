import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9671"
version_tuple = (0, 0, 9671)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9671")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9549"
data_version_tuple = (0, 0, 9549)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9549")
except ImportError:
    pass
data_git_hash = "c2f47bc747ebdc9daed7b00e1d603a73a2f1c58b"
data_git_describe = "v0.0-9549-gc2f47bc74"
data_git_msg = """\
commit c2f47bc747ebdc9daed7b00e1d603a73a2f1c58b
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Jan 20 15:28:27 2022 +0100

    [aes/pre_syn] Apply keep_hierarchy constraints to all prims not just buf
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
