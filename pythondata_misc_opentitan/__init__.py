import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9568"
version_tuple = (0, 0, 9568)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9568")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9446"
data_version_tuple = (0, 0, 9446)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9446")
except ImportError:
    pass
data_git_hash = "db0b4cea41217ccca01060f31b2ff1298c64bf86"
data_git_describe = "v0.0-9446-gdb0b4cea4"
data_git_msg = """\
commit db0b4cea41217ccca01060f31b2ff1298c64bf86
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Dec 14 18:33:33 2021 +0000

    [otbn,dv] Add coverage for scratchpad memory
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
