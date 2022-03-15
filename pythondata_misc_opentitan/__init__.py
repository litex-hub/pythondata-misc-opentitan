import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10896"
version_tuple = (0, 0, 10896)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10896")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10770"
data_version_tuple = (0, 0, 10770)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10770")
except ImportError:
    pass
data_git_hash = "cb8755cbd9acc1d1ce4281c0d6d6e32f399987bc"
data_git_describe = "v0.0-10770-gcb8755cbd"
data_git_msg = """\
commit cb8755cbd9acc1d1ce4281c0d6d6e32f399987bc
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Mar 14 15:38:05 2022 -0700

    [dv/clkmgr] Fix trans unit handling
    
    The RTL removed a trans unit and changed each idle input to be mubi.
    This caused a major breakage in dv. This updates dv to handle the new
    interface.
    
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
