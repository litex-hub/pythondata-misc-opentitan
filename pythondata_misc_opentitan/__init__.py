import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5342"
version_tuple = (0, 0, 5342)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5342")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5247"
data_version_tuple = (0, 0, 5247)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5247")
except ImportError:
    pass
data_git_hash = "cc0dd2a769f5852b7301848a050531d91f347b41"
data_git_describe = "v0.0-5247-gcc0dd2a76"
data_git_msg = """\
commit cc0dd2a769f5852b7301848a050531d91f347b41
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Mar 10 15:55:58 2021 +0000

    [otbn] Add second EDN connection
    
    OTBN needs two connections, one for RND and URND. This purely adds the
    second EDN connection, RND and URND are not yet implemented.
    
    Fixes #5523
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
