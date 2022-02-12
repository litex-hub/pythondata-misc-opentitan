import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10270"
version_tuple = (0, 0, 10270)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10270")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10146"
data_version_tuple = (0, 0, 10146)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10146")
except ImportError:
    pass
data_git_hash = "5082c23ec1589ea7d90938c25b845526864a0dca"
data_git_describe = "v0.0-10146-g5082c23ec"
data_git_msg = """\
commit 5082c23ec1589ea7d90938c25b845526864a0dca
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Feb 9 16:45:39 2022 -0800

    [dv] corresponding sva update for reset timing change
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
