import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10856"
version_tuple = (0, 0, 10856)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10856")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10730"
data_version_tuple = (0, 0, 10730)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10730")
except ImportError:
    pass
data_git_hash = "266a448c729b0207cbbe17b383257e68d8c3b481"
data_git_describe = "v0.0-10730-g266a448c7"
data_git_msg = """\
commit 266a448c729b0207cbbe17b383257e68d8c3b481
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Mar 7 19:07:23 2022 -0800

    [dif/clkmgr] Add support for count measurements
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
