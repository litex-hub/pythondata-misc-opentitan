import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5107"
version_tuple = (0, 0, 5107)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5107")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5016"
data_version_tuple = (0, 0, 5016)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5016")
except ImportError:
    pass
data_git_hash = "50978abe1e2fd623cfd3693a5738f421fc349c92"
data_git_describe = "v0.0-5016-g50978abe1"
data_git_msg = """\
commit 50978abe1e2fd623cfd3693a5738f421fc349c92
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Feb 22 10:41:25 2021 -0800

    [top] Hardware rv_dm hw_debug_en
    
    - Temporarily address #5332
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
