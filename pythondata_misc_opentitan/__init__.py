import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10767"
version_tuple = (0, 0, 10767)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10767")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10641"
data_version_tuple = (0, 0, 10641)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10641")
except ImportError:
    pass
data_git_hash = "a46a190fdb95844884ab0c534525178692d3cdde"
data_git_describe = "v0.0-10641-ga46a190fd"
data_git_msg = """\
commit a46a190fdb95844884ab0c534525178692d3cdde
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 3 15:49:08 2022 +0000

    [otbn,dv] Remove unused variables from OTBN C++ support code
    
    Some of these have been hanging around for quite a while :-/
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
