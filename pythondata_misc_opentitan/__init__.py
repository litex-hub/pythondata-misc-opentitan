import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8713"
version_tuple = (0, 0, 8713)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8713")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8601"
data_version_tuple = (0, 0, 8601)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8601")
except ImportError:
    pass
data_git_hash = "8872015a077af8abc279852f40e0a4f2c1b84c06"
data_git_describe = "v0.0-8601-g8872015a0"
data_git_msg = """\
commit 8872015a077af8abc279852f40e0a4f2c1b84c06
Author: Luís Marques <luismarques@lowrisc.org>
Date:   Sun Nov 14 22:28:36 2021 +0000

    [sw] Fix inline functions without linking location
    
    When creating builds with optimizations disabled (`-O0`) or with just
    inlining disabled (e.g. `-fno-inline`) there would be linking errors
    due to inline functions missing the corresponding extern declaration
    and thus not having linking locations. This fixes such errors, by
    adding the missing declarations and library dependencies. It also
    improves the consistency of those declarations, e.g. by adding the
    usual explanatory comment where it was missing.
    
    Signed-off-by: Luís Marques <luismarques@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
