import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14910"
version_tuple = (0, 0, 14910)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14910")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14768"
data_version_tuple = (0, 0, 14768)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14768")
except ImportError:
    pass
data_git_hash = "78427d34d369924c12bad37827d7988bd451986c"
data_git_describe = "v0.0-14768-g78427d34d3"
data_git_msg = """\
commit 78427d34d369924c12bad37827d7988bd451986c
Author: James Wainwright <james.wainwright@lowrisc.org>
Date:   Fri Oct 21 17:51:07 2022 +0100

    [flash_ctrl] Add unit test for flash_ctrl_info_erase
    
    Signed-off-by: James Wainwright <james.wainwright@lowrisc.org>

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
