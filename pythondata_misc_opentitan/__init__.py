import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10716"
version_tuple = (0, 0, 10716)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10716")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10590"
data_version_tuple = (0, 0, 10590)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10590")
except ImportError:
    pass
data_git_hash = "19270bbccdac0de939e677360b9abf40339099af"
data_git_describe = "v0.0-10590-g19270bbcc"
data_git_msg = """\
commit 19270bbccdac0de939e677360b9abf40339099af
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Thu Mar 3 10:56:25 2022 -0500

    [sw, base] Remove _ATTR_ from the attribute macros that have it, for consistency
    
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
