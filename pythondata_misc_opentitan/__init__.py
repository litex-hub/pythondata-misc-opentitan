import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11113"
version_tuple = (0, 0, 11113)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11113")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10987"
data_version_tuple = (0, 0, 10987)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10987")
except ImportError:
    pass
data_git_hash = "4b186e06d80305601974c3625f040993f460ec1e"
data_git_describe = "v0.0-10987-g4b186e06d"
data_git_msg = """\
commit 4b186e06d80305601974c3625f040993f460ec1e
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Mar 23 21:31:47 2022 -0700

    [cdc] Report per uniquified module
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
