import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8861"
version_tuple = (0, 0, 8861)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8861")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8749"
data_version_tuple = (0, 0, 8749)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8749")
except ImportError:
    pass
data_git_hash = "62ea9c4319395963d158b39e5a0c07a12c414357"
data_git_describe = "v0.0-8749-g62ea9c431"
data_git_msg = """\
commit 62ea9c4319395963d158b39e5a0c07a12c414357
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Nov 24 14:23:16 2021 -0800

    [chip, dv] Randomize SRAM
    
    Fixes private CI.
    Unconditionally initialize the SRAM with garbage data on reset for chip
    level SW based tests.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
