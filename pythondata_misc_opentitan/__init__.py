import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12292"
version_tuple = (0, 0, 12292)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12292")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12164"
data_version_tuple = (0, 0, 12164)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12164")
except ImportError:
    pass
data_git_hash = "d7325402e8b86c5df9c79d19c37587df2a356797"
data_git_describe = "v0.0-12164-gd7325402e"
data_git_msg = """\
commit d7325402e8b86c5df9c79d19c37587df2a356797
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon May 23 13:47:12 2022 +0200

    [fpga, doc, util] Remove refs and utils related to NexysVideo FPGA board
    
    The ChipWhisperer CW310 board is the main FPGA development board for
    OpenTitan. It has been decided to drop support for the NexysVideo board,
    see lowRISC/OpenTitan#7814. Thus, this commit removes references to
    the NexysVideo board from the documentation as well as tooling and
    utilities specific to the NexysVideo board.
    
    This is related to lowRISC/OpenTitan#12221.
    This resolves lowRISC/OpenTitan#12185.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
