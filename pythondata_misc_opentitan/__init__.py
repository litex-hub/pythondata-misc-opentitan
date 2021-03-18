import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5450"
version_tuple = (0, 0, 5450)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5450")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5355"
data_version_tuple = (0, 0, 5355)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5355")
except ImportError:
    pass
data_git_hash = "d2d7608cafffb82230fd8c55df32a2d57a4558c4"
data_git_describe = "v0.0-5355-gd2d7608ca"
data_git_msg = """\
commit d2d7608cafffb82230fd8c55df32a2d57a4558c4
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Mar 17 16:24:50 2021 -0700

    [lc_ctrl] Transition into D2
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
