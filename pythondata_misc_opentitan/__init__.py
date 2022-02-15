import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10304"
version_tuple = (0, 0, 10304)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10304")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10178"
data_version_tuple = (0, 0, 10178)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10178")
except ImportError:
    pass
data_git_hash = "2ff8a74d5ac6a5d028a1da0e093739950514207f"
data_git_describe = "v0.0-10178-g2ff8a74d5"
data_git_msg = """\
commit 2ff8a74d5ac6a5d028a1da0e093739950514207f
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Thu Feb 10 12:24:45 2022 +0000

    [lc_ctrl] Moved to V2
    
    - Updated project to V2
    - Updated note regarding RV_TAP
    - Added caveat regarding condition coverage to checklist
    
    Signed-off-by: Nigel Scales <nigel.scales@gmail.com>

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
