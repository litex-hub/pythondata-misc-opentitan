import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14128"
version_tuple = (0, 0, 14128)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14128")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13986"
data_version_tuple = (0, 0, 13986)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13986")
except ImportError:
    pass
data_git_hash = "863be67224777cbf2da1c520af0745631108614e"
data_git_describe = "v0.0-13986-g863be67224"
data_git_msg = """\
commit 863be67224777cbf2da1c520af0745631108614e
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Sep 9 16:35:07 2022 -0400

    [test] Add rom_e2e_bootstrap_phase1_read
    
    Fixes #14462
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
