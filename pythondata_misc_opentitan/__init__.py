import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11406"
version_tuple = (0, 0, 11406)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11406")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11280"
data_version_tuple = (0, 0, 11280)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11280")
except ImportError:
    pass
data_git_hash = "a491a03422dbc4f381207910f00ca6507e0bf4a2"
data_git_describe = "v0.0-11280-ga491a0342"
data_git_msg = """\
commit a491a03422dbc4f381207910f00ca6507e0bf4a2
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue Mar 29 10:08:36 2022 +0100

    [Otbn, dv] Added otbn_zero_state_err_urnd testcase
    
    This commit adds otbn_zero_state_err_urnd testcase and all the necessary
    changes required to run it.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
