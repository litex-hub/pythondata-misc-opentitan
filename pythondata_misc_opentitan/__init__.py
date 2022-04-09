import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11495"
version_tuple = (0, 0, 11495)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11495")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11369"
data_version_tuple = (0, 0, 11369)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11369")
except ImportError:
    pass
data_git_hash = "ef74184eb4a8dc7e48fa081cfb7671df30dcce77"
data_git_describe = "v0.0-11369-gef74184eb"
data_git_msg = """\
commit ef74184eb4a8dc7e48fa081cfb7671df30dcce77
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Apr 6 22:13:35 2022 -0700

    [lc_ctrl] Ensure inconsistent token mux triggers TRANSITION_ERROR
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
