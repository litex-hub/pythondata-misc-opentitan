import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13208"
version_tuple = (0, 0, 13208)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13208")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13066"
data_version_tuple = (0, 0, 13066)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13066")
except ImportError:
    pass
data_git_hash = "733ebb6022ebceca3fdb3e97fb174d0102d5eeb7"
data_git_describe = "v0.0-13066-g733ebb6022"
data_git_msg = """\
commit 733ebb6022ebceca3fdb3e97fb174d0102d5eeb7
Author: Michael Schaffner <msf@google.com>
Date:   Wed Jul 20 17:03:39 2022 -0700

    [rom_ctrl] Enable secure FIFO counters
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
