import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5199"
version_tuple = (0, 0, 5199)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5199")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5108"
data_version_tuple = (0, 0, 5108)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5108")
except ImportError:
    pass
data_git_hash = "ce5945d14f94baa796b88a8df69bdaa428a903a7"
data_git_describe = "v0.0-5108-gce5945d14"
data_git_msg = """\
commit ce5945d14f94baa796b88a8df69bdaa428a903a7
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Tue Mar 2 14:50:18 2021 +0000

    [aon_timer] Lint fixes
    
    Fix a few signal warnings picked up by Ascent lint.
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
