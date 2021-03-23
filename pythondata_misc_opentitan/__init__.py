import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5533"
version_tuple = (0, 0, 5533)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5533")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5438"
data_version_tuple = (0, 0, 5438)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5438")
except ImportError:
    pass
data_git_hash = "f89627f2929fa7fa38db8f9bf21279e549612a17"
data_git_describe = "v0.0-5438-gf89627f29"
data_git_msg = """\
commit f89627f2929fa7fa38db8f9bf21279e549612a17
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 23 14:03:29 2021 +0000

    [pwrmgr] Waive Verilator lint warning about "abort" name
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
