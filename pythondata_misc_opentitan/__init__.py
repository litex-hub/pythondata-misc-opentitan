import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5219"
version_tuple = (0, 0, 5219)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5219")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5128"
data_version_tuple = (0, 0, 5128)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5128")
except ImportError:
    pass
data_git_hash = "0e0a74b20fa83fa84b5169f8a0781c2d17db02bb"
data_git_describe = "v0.0-5128-g0e0a74b20"
data_git_msg = """\
commit 0e0a74b20fa83fa84b5169f8a0781c2d17db02bb
Author: Eitan Shapira <eitan.shapira@nuvoton.com>
Date:   Mon Mar 1 17:17:48 2021 +0200

    [dv/flash_ctrl] Changes to integrate vendor environment
    
    Signed-off-by: Eitan Shapira <eitan.shapira@nuvoton.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
