import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5198"
version_tuple = (0, 0, 5198)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5198")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5107"
data_version_tuple = (0, 0, 5107)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5107")
except ImportError:
    pass
data_git_hash = "b801ad46d6426401d202310fb79b85e6430fb284"
data_git_describe = "v0.0-5107-gb801ad46d"
data_git_msg = """\
commit b801ad46d6426401d202310fb79b85e6430fb284
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Fri Feb 26 16:10:33 2021 +0000

    [aon_timer] Advance to D1 status
    
    The IP is already instantiated in top_earlygrey and all checklist items
    are complete.
    
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
