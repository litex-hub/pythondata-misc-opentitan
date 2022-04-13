import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11555"
version_tuple = (0, 0, 11555)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11555")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11429"
data_version_tuple = (0, 0, 11429)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11429")
except ImportError:
    pass
data_git_hash = "937c6a83e84a6eaaf6eaff00c43a5b8ad429e986"
data_git_describe = "v0.0-11429-g937c6a83e"
data_git_msg = """\
commit 937c6a83e84a6eaaf6eaff00c43a5b8ad429e986
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Apr 12 15:05:43 2022 -0700

    [doc] Minor fix to sensor_ctrl sw markdown
    
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
