import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13202"
version_tuple = (0, 0, 13202)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13202")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13060"
data_version_tuple = (0, 0, 13060)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13060")
except ImportError:
    pass
data_git_hash = "45f56546c54cae125a8c7bd077cdf596adb27940"
data_git_describe = "v0.0-13060-g45f56546c5"
data_git_msg = """\
commit 45f56546c54cae125a8c7bd077cdf596adb27940
Author: Michael Schaffner <msf@google.com>
Date:   Wed Jul 20 16:54:53 2022 -0700

    [tlul_adapter_sram] Update comment describing the ByteAccess parameter
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
