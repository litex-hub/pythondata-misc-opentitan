import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11040"
version_tuple = (0, 0, 11040)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11040")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10914"
data_version_tuple = (0, 0, 10914)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10914")
except ImportError:
    pass
data_git_hash = "d7f048e471b6da4ff0b7283be47572ce90b6558f"
data_git_describe = "v0.0-10914-gd7f048e47"
data_git_msg = """\
commit d7f048e471b6da4ff0b7283be47572ce90b6558f
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Mar 23 10:36:03 2022 -0700

    [otp_ctrl] Correct description to reflect current behavior
    
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
