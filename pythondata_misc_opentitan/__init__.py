import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10838"
version_tuple = (0, 0, 10838)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10838")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10712"
data_version_tuple = (0, 0, 10712)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10712")
except ImportError:
    pass
data_git_hash = "d361da6a10ba99cf7c67798f362d324b1ef0885f"
data_git_describe = "v0.0-10712-gd361da6a1"
data_git_msg = """\
commit d361da6a10ba99cf7c67798f362d324b1ef0885f
Author: Michael Schaffner <msf@google.com>
Date:   Thu Mar 10 16:19:05 2022 -0800

    [tlul_lc_gate] Fix gating condition
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
