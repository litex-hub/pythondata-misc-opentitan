import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8311"
version_tuple = (0, 0, 8311)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8311")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8199"
data_version_tuple = (0, 0, 8199)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8199")
except ImportError:
    pass
data_git_hash = "727f1312ea6602e586ff0b34029dd674c22e7ab6"
data_git_describe = "v0.0-8199-g727f1312e"
data_git_msg = """\
commit 727f1312ea6602e586ff0b34029dd674c22e7ab6
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Oct 13 09:43:09 2021 -0700

    [opentitantool] Support bitstream loading on the CW310 board
    
    1. Add an fpga_program function to the Transport trait.
    2. Add the bitstream programming procedure to the CW310 backend.
    3. Add a CLI command to program the bitstream.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
