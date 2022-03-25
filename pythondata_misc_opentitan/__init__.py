import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11131"
version_tuple = (0, 0, 11131)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11131")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11005"
data_version_tuple = (0, 0, 11005)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11005")
except ImportError:
    pass
data_git_hash = "6f175ff0647397152607c676ee50ed75fa5bba6c"
data_git_describe = "v0.0-11005-g6f175ff06"
data_git_msg = """\
commit 6f175ff0647397152607c676ee50ed75fa5bba6c
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 24 19:24:35 2022 -0700

    [sensor_ctrl] Move to D2
    
    - also add missing checklist
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
