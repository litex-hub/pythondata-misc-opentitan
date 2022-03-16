import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10911"
version_tuple = (0, 0, 10911)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10911")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10785"
data_version_tuple = (0, 0, 10785)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10785")
except ImportError:
    pass
data_git_hash = "0eef86cff5b94f577153640ac78a9fa4f56ccc54"
data_git_describe = "v0.0-10785-g0eef86cff"
data_git_msg = """\
commit 0eef86cff5b94f577153640ac78a9fa4f56ccc54
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Mar 14 19:27:12 2022 -0700

    [keymgr] Minor refactor for long files
    
    - move data fsm, op fsm and error collection into their own
      separate modules.
    - also some minor clean-up.
    
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
