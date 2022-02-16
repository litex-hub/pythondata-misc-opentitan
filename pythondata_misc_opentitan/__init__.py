import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10354"
version_tuple = (0, 0, 10354)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10354")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10228"
data_version_tuple = (0, 0, 10228)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10228")
except ImportError:
    pass
data_git_hash = "bbb36c003493e88fe4c1160594bd5ad686177e8c"
data_git_describe = "v0.0-10228-gbbb36c003"
data_git_msg = """\
commit bbb36c003493e88fe4c1160594bd5ad686177e8c
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Fri Feb 11 09:17:50 2022 -0800

    [csrng/dv] Verify lc_hw_debug_en and cs_aes_halt
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
