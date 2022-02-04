import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10072"
version_tuple = (0, 0, 10072)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10072")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9948"
data_version_tuple = (0, 0, 9948)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9948")
except ImportError:
    pass
data_git_hash = "2b9e1d6126690054fc73799fe017cf2234756dc2"
data_git_describe = "v0.0-9948-g2b9e1d612"
data_git_msg = """\
commit 2b9e1d6126690054fc73799fe017cf2234756dc2
Author: Alexander Williams <awill@google.com>
Date:   Thu Feb 3 16:01:28 2022 -0800

    [reg_tool] Remove unused signals for sw wo access
    
    For fields using the async parameter, undriven 'qs' signals would be
    generated, causing linter errors and 'X' origination. Check for read
    access and limit code generation for 'qs' signals to when that is true.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
