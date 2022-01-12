import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9487"
version_tuple = (0, 0, 9487)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9487")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9369"
data_version_tuple = (0, 0, 9369)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9369")
except ImportError:
    pass
data_git_hash = "99cbf0c060642c0389dbf1710c9cc98673f1db86"
data_git_describe = "v0.0-9369-g99cbf0c06"
data_git_msg = """\
commit 99cbf0c060642c0389dbf1710c9cc98673f1db86
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Jan 12 15:04:21 2022 +0000

    [usbdev] Add lint waiver
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
