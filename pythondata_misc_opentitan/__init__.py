import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8401"
version_tuple = (0, 0, 8401)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8401")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8289"
data_version_tuple = (0, 0, 8289)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8289")
except ImportError:
    pass
data_git_hash = "a538a01fe666f073e38b7252353163fd35702e48"
data_git_describe = "v0.0-8289-ga538a01fe"
data_git_msg = """\
commit a538a01fe666f073e38b7252353163fd35702e48
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Oct 21 23:23:34 2021 +0000

    [dif/clkmgr] Fix broken unit tests.
    
    The clkmgr DIF unit tests were stale since the DIF *_params_t struct
    deprecation that took place as a result of #8409 and the meson build
    target was not correct so the stale unit tests were not causing a build
    failure. This change fixes that.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
