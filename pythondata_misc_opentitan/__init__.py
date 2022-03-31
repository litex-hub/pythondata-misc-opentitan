import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11249"
version_tuple = (0, 0, 11249)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11249")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11123"
data_version_tuple = (0, 0, 11123)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11123")
except ImportError:
    pass
data_git_hash = "0747afbddec0ad176980429fe3100b32edb71d4a"
data_git_describe = "v0.0-11123-g0747afbdd"
data_git_msg = """\
commit 0747afbddec0ad176980429fe3100b32edb71d4a
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Wed Mar 30 17:09:19 2022 +0100

    [dv] Enable C/C++ code sourcing with VCS in .core
    
    Apparently fusesoc is not properly sourcing C/C++ files.
    Manually adding the generated directories solves the issue.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
