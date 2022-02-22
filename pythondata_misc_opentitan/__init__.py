import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10465"
version_tuple = (0, 0, 10465)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10465")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10339"
data_version_tuple = (0, 0, 10339)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10339")
except ImportError:
    pass
data_git_hash = "8bb8cc98c47a3b63e4a528005f3fdbd3b728fdb2"
data_git_describe = "v0.0-10339-g8bb8cc98c"
data_git_msg = """\
commit 8bb8cc98c47a3b63e4a528005f3fdbd3b728fdb2
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue Feb 22 11:12:23 2022 +0000

    [rom_ctrl, dv] Fix for rom_ctrl_kmac_err_chk regression failure
    
    Fatal alert is not triggered unless error response is signalled from
    Kmac. Kmac signals an error only after kmac_data_o.last is asserted.
    Last is asserted after all the address spaces in the rom is read and
    sent to KMAC. Ths depends on the delay between ready-valid handshake.
    Therefore, delay to expect the alert has been increased to ensure that
    we wait till last has been asserted.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
