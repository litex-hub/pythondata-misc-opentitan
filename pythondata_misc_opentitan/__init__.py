import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14502"
version_tuple = (0, 0, 14502)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14502")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14360"
data_version_tuple = (0, 0, 14360)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14360")
except ImportError:
    pass
data_git_hash = "1a4303f143565bd52df87bb5e8b25c5a729e49eb"
data_git_describe = "v0.0-14360-g1a4303f143"
data_git_msg = """\
commit 1a4303f143565bd52df87bb5e8b25c5a729e49eb
Author: Weicai Yang <weicai@google.com>
Date:   Wed Sep 28 17:19:19 2022 -0700

    [spi_device/dv] Fix flash mode failures
    
    Fixed failures due to recent updates
    1. `output` doesn't work for a task if it's killed, changed to `ref`
    2. The address order was updated wrongly
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
