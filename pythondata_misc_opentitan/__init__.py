import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8414"
version_tuple = (0, 0, 8414)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8414")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8302"
data_version_tuple = (0, 0, 8302)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8302")
except ImportError:
    pass
data_git_hash = "adf65e9308ff21c14643560955cc823c260a00bf"
data_git_describe = "v0.0-8302-gadf65e930"
data_git_msg = """\
commit adf65e9308ff21c14643560955cc823c260a00bf
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Oct 21 14:24:04 2021 -0700

    [dv/format] Clean verible format issues
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
