import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5830"
version_tuple = (0, 0, 5830)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5830")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5735"
data_version_tuple = (0, 0, 5735)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5735")
except ImportError:
    pass
data_git_hash = "a6b5a1e33f5164f45812839f4f32430ee2a60c26"
data_git_describe = "v0.0-5735-ga6b5a1e33"
data_git_msg = """\
commit a6b5a1e33f5164f45812839f4f32430ee2a60c26
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Apr 12 14:20:30 2021 -0700

    [top] Turn on secure ibex for asic
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
