import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14137"
version_tuple = (0, 0, 14137)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14137")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13995"
data_version_tuple = (0, 0, 13995)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13995")
except ImportError:
    pass
data_git_hash = "d6398dd297e6945dbb164bbca25ce926c9787270"
data_git_describe = "v0.0-13995-gd6398dd297"
data_git_msg = """\
commit d6398dd297e6945dbb164bbca25ce926c9787270
Author: Miles Dai <milesdai@google.com>
Date:   Tue Aug 30 16:38:16 2022 -0400

    [doc] Update commands for connecting to FPGA with openOCD
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
