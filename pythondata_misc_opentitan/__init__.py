import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10220"
version_tuple = (0, 0, 10220)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10220")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10096"
data_version_tuple = (0, 0, 10096)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10096")
except ImportError:
    pass
data_git_hash = "6b6ed4590aa6c665e2512d42360eec1be39cb415"
data_git_describe = "v0.0-10096-g6b6ed4590"
data_git_msg = """\
commit 6b6ed4590aa6c665e2512d42360eec1be39cb415
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Wed Feb 9 12:33:58 2022 +0100

    [aes] Re-enable synthesis optimizations for FWD/INV-only core instances
    
    This commit moves the prim_buf on the cipher core operation signal to
    the outside of the cipher core. Having this prim_buf inside the cipher
    core prevents synthesis from performing area optimizations if only
    forward or inverse operation is needed for a particular cipher core
    instance (see e.g. CSRNG).
    
    This is related to lowRISC/OpenTitan#10483.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
