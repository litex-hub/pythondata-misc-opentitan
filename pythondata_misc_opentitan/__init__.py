import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8199"
version_tuple = (0, 0, 8199)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8199")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8087"
data_version_tuple = (0, 0, 8087)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8087")
except ImportError:
    pass
data_git_hash = "ec41b22863383ac23f2834089c002d5fca009f75"
data_git_describe = "v0.0-8087-gec41b2286"
data_git_msg = """\
commit ec41b22863383ac23f2834089c002d5fca009f75
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Oct 11 10:56:08 2021 +0100

    [otbn,dv] Add utility functions to otbn_env_cfg for IMEM access
    
    These do the (de)scrambling required to do reads and writes. We don't
    yet do the DMEM side (because we haven't got a use case for it yet).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
