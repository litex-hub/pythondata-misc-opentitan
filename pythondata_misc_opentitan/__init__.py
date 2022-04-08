import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11481"
version_tuple = (0, 0, 11481)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11481")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11355"
data_version_tuple = (0, 0, 11355)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11355")
except ImportError:
    pass
data_git_hash = "a08273a6996906e0e68372a72ac838cd23346594"
data_git_describe = "v0.0-11355-ga08273a69"
data_git_msg = """\
commit a08273a6996906e0e68372a72ac838cd23346594
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Apr 7 10:36:58 2022 -0700

    [rv_core_ibex, top] Make USR_ACCESS available to software
    
    - fixes #11964
    
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
