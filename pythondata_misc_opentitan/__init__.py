import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15325"
version_tuple = (0, 0, 15325)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15325")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15183"
data_version_tuple = (0, 0, 15183)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15183")
except ImportError:
    pass
data_git_hash = "9899bab796c8761eb9b7a85534808730af1c1bfc"
data_git_describe = "v0.0-15183-g9899bab796"
data_git_msg = """\
commit 9899bab796c8761eb9b7a85534808730af1c1bfc
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Nov 7 15:24:26 2022 -0800

    [dv,test] fix `rom_e2e_shutdown_exception_c` test
    
    This fixes the `rom_e2e_shutdown_exception_c` test by implementing a
    sequence to check the UART output for a specific boot fault message,
    since the ROM does not allow use of the DV backdoor logging mechanism.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
