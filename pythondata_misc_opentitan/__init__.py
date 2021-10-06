import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8147"
version_tuple = (0, 0, 8147)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8147")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8039"
data_version_tuple = (0, 0, 8039)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8039")
except ImportError:
    pass
data_git_hash = "81f262b7a76716d92a63502bb8da3d51a2d50411"
data_git_describe = "v0.0-8039-g81f262b7a"
data_git_msg = """\
commit 81f262b7a76716d92a63502bb8da3d51a2d50411
Author: Eitan Shapira <eitanshapira89@gmail.com>
Date:   Wed Oct 6 16:09:34 2021 +0300

    [flash_ctrl/dv] Make bank erase to be selectable by default
    
    Signed-off-by: Eitan Shapira <eitanshapira89@gmail.com>

"""

# Tool version info
tool_version_str = "0.0.post108"
tool_version_tuple = (0, 0, 108)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post108")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
