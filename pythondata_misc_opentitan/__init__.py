import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13282"
version_tuple = (0, 0, 13282)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13282")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13140"
data_version_tuple = (0, 0, 13140)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13140")
except ImportError:
    pass
data_git_hash = "f283b981ea26e9900f5242e64d1a4a0a43d00cfa"
data_git_describe = "v0.0-13140-gf283b981ea"
data_git_msg = """\
commit f283b981ea26e9900f5242e64d1a4a0a43d00cfa
Author: Srinivasan Y <srinivasan.yadhunathan@seagate.com>
Date:   Tue Jul 26 20:55:55 2022 +0800

    [sw,crypto] Update crypto API header against the latest crypto spec
    
    The crypto API header is now updated against the latest crypto specification [v3], as of 26Jul2022
    
    Signed-off-by: Srinivasan Y <srinivasan.yadhunathan@seagate.com>

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
