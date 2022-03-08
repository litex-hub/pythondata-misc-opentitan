import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10782"
version_tuple = (0, 0, 10782)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10782")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10656"
data_version_tuple = (0, 0, 10656)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10656")
except ImportError:
    pass
data_git_hash = "1938c40267b74458d3f0a7b80892ac9921424bd9"
data_git_describe = "v0.0-10656-g1938c4026"
data_git_msg = """\
commit 1938c40267b74458d3f0a7b80892ac9921424bd9
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 1 16:33:44 2022 -0800

    [clkmgr, top] clkmgr and top updates to better support ast external clock
    
    - ast provides a direct indication whether clock dividers should be stepped
      down during an external switch.
    
    - clkmgr can make use of this mechanism directly without having to piece
      separate logic together.
    
    - This PR may be incomplete at the moment because the relevant signals are
      in an async domain, this may be changed by an AST update.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
