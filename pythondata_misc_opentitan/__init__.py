import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8818"
version_tuple = (0, 0, 8818)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8818")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8706"
data_version_tuple = (0, 0, 8706)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8706")
except ImportError:
    pass
data_git_hash = "686deb7fd40e73798fd434dbbde05b02840e7c78"
data_git_describe = "v0.0-8706-g686deb7fd"
data_git_msg = """\
commit 686deb7fd40e73798fd434dbbde05b02840e7c78
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Nov 22 16:35:37 2021 +0000

    [rom_ctrl] Update checklist to match current status
    
    Everything is done for D2 except the planning/implementation of
    FI hardening and countermeasures.
    
    The LINT_PASS item includes a review of lint waivers. There's exactly
    one such waiver, which silences AscentLint about a signal that's
    intentionally driven to a constant, one cycle after reset (the world's
    simplest FSM!)
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
