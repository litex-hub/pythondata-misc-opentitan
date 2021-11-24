import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8849"
version_tuple = (0, 0, 8849)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8849")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8737"
data_version_tuple = (0, 0, 8737)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8737")
except ImportError:
    pass
data_git_hash = "76169d8b09eca887925d328d9d8cd22bbac610ab"
data_git_describe = "v0.0-8737-g76169d8b0"
data_git_msg = """\
commit 76169d8b09eca887925d328d9d8cd22bbac610ab
Author: Weicai Yang <weicai@google.com>
Date:   Mon Nov 22 16:16:47 2021 -0800

    [keymgr/dv] Disable assertion data stable check
    
    Addressed #9324
    Disabled the assertion when it's in StDisabled/StInvalid, LC is off or
    SW/HW input is invalid
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
