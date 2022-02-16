import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10363"
version_tuple = (0, 0, 10363)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10363")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10237"
data_version_tuple = (0, 0, 10237)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10237")
except ImportError:
    pass
data_git_hash = "85dbfb665b5f813d01ed979d997039cd3dd50de3"
data_git_describe = "v0.0-10237-g85dbfb665"
data_git_msg = """\
commit 85dbfb665b5f813d01ed979d997039cd3dd50de3
Author: Weicai Yang <weicai@google.com>
Date:   Mon Feb 14 21:59:33 2022 -0800

    [prim] Move sec_cm assertion to an include file in prim_assert
    
    Addressed problem raised in #10248 - Yosys only allows macros to be in
    an included file
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
