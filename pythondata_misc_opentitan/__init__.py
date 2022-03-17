import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10938"
version_tuple = (0, 0, 10938)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10938")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10812"
data_version_tuple = (0, 0, 10812)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10812")
except ImportError:
    pass
data_git_hash = "ef7251a509edea71b16b00af64c363f72e224dd8"
data_git_describe = "v0.0-10812-gef7251a50"
data_git_msg = """\
commit ef7251a509edea71b16b00af64c363f72e224dd8
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Wed Mar 16 14:58:37 2022 -0400

    [sw] Get rid of bespoke *_WARN_UNUSED_RESULT macros
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

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
