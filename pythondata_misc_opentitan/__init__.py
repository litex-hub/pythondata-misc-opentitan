import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10802"
version_tuple = (0, 0, 10802)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10802")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10676"
data_version_tuple = (0, 0, 10676)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10676")
except ImportError:
    pass
data_git_hash = "87c41e52d089527095e7df84931df5f2a550f3ce"
data_git_describe = "v0.0-10676-g87c41e52d"
data_git_msg = """\
commit 87c41e52d089527095e7df84931df5f2a550f3ce
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Mar 4 20:31:31 2022 +0000

    [dv,top,pwm] top sleep pwm pulses test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
