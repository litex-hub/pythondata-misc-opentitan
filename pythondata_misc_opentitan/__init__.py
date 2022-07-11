import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13008"
version_tuple = (0, 0, 13008)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13008")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12866"
data_version_tuple = (0, 0, 12866)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12866")
except ImportError:
    pass
data_git_hash = "6617ebbb5027b8ea76c0090a8bf896ed228b72a2"
data_git_describe = "v0.0-12866-g6617ebbb50"
data_git_msg = """\
commit 6617ebbb5027b8ea76c0090a8bf896ed228b72a2
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Jul 7 17:07:15 2022 +0200

    [otbn] Add prim_onehot_mux to logical operation output in bignum ALU
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
