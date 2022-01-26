import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9802"
version_tuple = (0, 0, 9802)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9802")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9680"
data_version_tuple = (0, 0, 9680)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9680")
except ImportError:
    pass
data_git_hash = "5556d17ed47aeed5ea88a4480d9b4d8fb2aeb751"
data_git_describe = "v0.0-9680-g5556d17ed"
data_git_msg = """\
commit 5556d17ed47aeed5ea88a4480d9b4d8fb2aeb751
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Jan 25 15:47:43 2022 -0800

    [spi_device] Update prj.hjson to D2
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
