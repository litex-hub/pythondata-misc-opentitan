import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11156"
version_tuple = (0, 0, 11156)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11156")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11030"
data_version_tuple = (0, 0, 11030)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11030")
except ImportError:
    pass
data_git_hash = "8d507ad3f9dc47705b292a8e9568f73b772976ed"
data_git_describe = "v0.0-11030-g8d507ad3f"
data_git_msg = """\
commit 8d507ad3f9dc47705b292a8e9568f73b772976ed
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Mar 24 16:32:08 2022 +0100

    [aes] Fix clearing of data input registers
    
    Previously, the write enable for the data input registers was set for
    two clock cycles when clearing the registers. This caused the
    data_in_qe_i signals used for status tracking to be high during the
    first clock cycle when back in IDLE. As a result, the AES unit would
    immediately start when running in automatic operation.
    
    This is related to lowRISC/OpenTitan#11431.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
