import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8680"
version_tuple = (0, 0, 8680)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8680")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8568"
data_version_tuple = (0, 0, 8568)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8568")
except ImportError:
    pass
data_git_hash = "44caf3b591ce164fad50dea6f22f769f65c399ca"
data_git_describe = "v0.0-8568-g44caf3b59"
data_git_msg = """\
commit 44caf3b591ce164fad50dea6f22f769f65c399ca
Author: Alphan Ulusoy <alphan@google.com>
Date:   Mon Nov 8 17:57:20 2021 -0500

    [sw/silicon_creator] Remove is_busy() from flash_ctrl driver
    
    Since all operations are blocking, we don't need to check if the flash
    controller is busy before starting a new operation.
    
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
