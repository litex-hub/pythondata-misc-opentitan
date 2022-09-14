import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14199"
version_tuple = (0, 0, 14199)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14199")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14057"
data_version_tuple = (0, 0, 14057)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14057")
except ImportError:
    pass
data_git_hash = "a6bc82ee68ded1144c0dcf637a67e12eeec00294"
data_git_describe = "v0.0-14057-ga6bc82ee68"
data_git_msg = """\
commit a6bc82ee68ded1144c0dcf637a67e12eeec00294
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Sep 14 11:58:30 2022 -0700

    [bazel] fix airgapped directory generation script
    
    Turns out #14860 requires an update to this script.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
