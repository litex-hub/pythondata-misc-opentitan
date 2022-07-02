import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12931"
version_tuple = (0, 0, 12931)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12931")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12789"
data_version_tuple = (0, 0, 12789)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12789")
except ImportError:
    pass
data_git_hash = "0cc1e439b562ab1dffc5ce85ab4ad2a48b4245ee"
data_git_describe = "v0.0-12789-g0cc1e439b5"
data_git_msg = """\
commit 0cc1e439b562ab1dffc5ce85ab4ad2a48b4245ee
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Jul 1 11:19:52 2022 -0700

    [formal,conn] Add ast to entropy_src connectivity check
    
    Also fix path to usbdev ram.
    
    Fixes #13460
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
