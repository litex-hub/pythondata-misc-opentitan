import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8760"
version_tuple = (0, 0, 8760)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8760")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8648"
data_version_tuple = (0, 0, 8648)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8648")
except ImportError:
    pass
data_git_hash = "5aaad4e1c47c92290582d566c76a3d54c6c0fa50"
data_git_describe = "v0.0-8648-g5aaad4e1c"
data_git_msg = """\
commit 5aaad4e1c47c92290582d566c76a3d54c6c0fa50
Author: Weicai Yang <weicai@google.com>
Date:   Tue Nov 16 23:45:28 2021 -0800

    [cleanup] Remove mubi4_e and replace it with mubi4_t
    
    also do the same for mubi8/16
    Signed-off-by: Weicai Yang <weicai@google.com>

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
