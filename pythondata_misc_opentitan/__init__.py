import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10725"
version_tuple = (0, 0, 10725)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10725")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10599"
data_version_tuple = (0, 0, 10599)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10599")
except ImportError:
    pass
data_git_hash = "988d400251c547fd0b41bf7b8feb8543174d0ee5"
data_git_describe = "v0.0-10599-g988d40025"
data_git_msg = """\
commit 988d400251c547fd0b41bf7b8feb8543174d0ee5
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 3 16:21:53 2022 -0800

    [flash_ctrl] Fix init_busy glitches
    
    - identified by weicai in #11235
    
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
