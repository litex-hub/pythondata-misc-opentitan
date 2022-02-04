import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10071"
version_tuple = (0, 0, 10071)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10071")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9947"
data_version_tuple = (0, 0, 9947)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9947")
except ImportError:
    pass
data_git_hash = "180c2536cd79881638b601e6a9857913dcd87888"
data_git_describe = "v0.0-9947-g180c2536c"
data_git_msg = """\
commit 180c2536cd79881638b601e6a9857913dcd87888
Author: Weicai Yang <weicai@google.com>
Date:   Thu Feb 3 15:40:18 2022 -0800

    [dv] Address 2 comments in sec_cm update PR
    
    For PR #10539
    1. removed unused CntStyle
    2. moved sec_cm_alert_name check to the top of the seq
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
