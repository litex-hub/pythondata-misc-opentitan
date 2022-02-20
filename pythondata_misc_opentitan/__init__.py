import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10454"
version_tuple = (0, 0, 10454)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10454")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10328"
data_version_tuple = (0, 0, 10328)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10328")
except ImportError:
    pass
data_git_hash = "bef5e3faab1cecfe04aacdbd8e73fe8f52790fe5"
data_git_describe = "v0.0-10328-gbef5e3faa"
data_git_msg = """\
commit bef5e3faab1cecfe04aacdbd8e73fe8f52790fe5
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Feb 18 13:06:07 2022 -0800

    [top] Hook-up flash/otp control and observation bus to ast
    
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
