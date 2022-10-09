import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14632"
version_tuple = (0, 0, 14632)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14632")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14490"
data_version_tuple = (0, 0, 14490)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14490")
except ImportError:
    pass
data_git_hash = "ef2c138e048e191c4fe9d3bba0bc4fd869346fd0"
data_git_describe = "v0.0-14490-gef2c138e04"
data_git_msg = """\
commit ef2c138e048e191c4fe9d3bba0bc4fd869346fd0
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Oct 7 21:38:58 2022 +0000

    [flash_ctrl,dv] flash_ctrl.ctrl_regwen test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
