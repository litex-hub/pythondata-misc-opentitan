import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5631"
version_tuple = (0, 0, 5631)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5631")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5536"
data_version_tuple = (0, 0, 5536)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5536")
except ImportError:
    pass
data_git_hash = "ffbfb492e072ffb8c8785452f6ded8b62035fc22"
data_git_describe = "v0.0-5536-gffbfb492e"
data_git_msg = """\
commit ffbfb492e072ffb8c8785452f6ded8b62035fc22
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Mar 26 14:59:47 2021 +0100

    [aes/doc] Add missing line breaks to correct formatting
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
