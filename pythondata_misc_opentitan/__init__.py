import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8653"
version_tuple = (0, 0, 8653)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8653")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8541"
data_version_tuple = (0, 0, 8541)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8541")
except ImportError:
    pass
data_git_hash = "261a12b15f8ec711aa4e14512787b11e3c08531e"
data_git_describe = "v0.0-8541-g261a12b15"
data_git_msg = """\
commit 261a12b15f8ec711aa4e14512787b11e3c08531e
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Nov 5 11:27:26 2021 -0400

    [sw/silicon_creator] Add info page layout table to flash_ctrl.h
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
