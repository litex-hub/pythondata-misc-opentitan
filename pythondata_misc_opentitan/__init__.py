import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9868"
version_tuple = (0, 0, 9868)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9868")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9744"
data_version_tuple = (0, 0, 9744)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9744")
except ImportError:
    pass
data_git_hash = "384ac7f243ccf6caab658ce9a0a3e6ff74ca2ffd"
data_git_describe = "v0.0-9744-g384ac7f24"
data_git_msg = """\
commit 384ac7f243ccf6caab658ce9a0a3e6ff74ca2ffd
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Jan 27 00:39:42 2022 -0800

    [dif/alert_handler] Enable actions after configs
    
    This commit alters the functionalities of the configuration DIFs for
    alerts, local alerts, and classes, by only enabling each feature *after*
    it has been configured. This is done since as soon as a feature is
    enabled, it is active.
    
    This partially addresses #9899.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
