import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10684"
version_tuple = (0, 0, 10684)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10684")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10558"
data_version_tuple = (0, 0, 10558)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10558")
except ImportError:
    pass
data_git_hash = "b45d6a63201b60554facb96d1799cd48ab0ea35e"
data_git_describe = "v0.0-10558-gb45d6a632"
data_git_msg = """\
commit b45d6a63201b60554facb96d1799cd48ab0ea35e
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Feb 18 14:37:48 2022 -0800

    [dv/pwrmgr] Fix lc/sys reset handshake SVAs
    
    Add support for a change in the request.
    
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
