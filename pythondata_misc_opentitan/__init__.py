import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12616"
version_tuple = (0, 0, 12616)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12616")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12474"
data_version_tuple = (0, 0, 12474)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12474")
except ImportError:
    pass
data_git_hash = "e169485e9dce49f15047bcfb4e02df606fea2019"
data_git_describe = "v0.0-12474-ge169485e9"
data_git_msg = """\
commit e169485e9dce49f15047bcfb4e02df606fea2019
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jun 9 07:50:57 2022 -0700

    [dv,chip_testplan] Add sleep frequency tests
    
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
