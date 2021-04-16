import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5895"
version_tuple = (0, 0, 5895)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5895")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5800"
data_version_tuple = (0, 0, 5800)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5800")
except ImportError:
    pass
data_git_hash = "bd9c77eac8f19a27de3c6e8e92235eab81937793"
data_git_describe = "v0.0-5800-gbd9c77eac"
data_git_msg = """\
commit bd9c77eac8f19a27de3c6e8e92235eab81937793
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 5 16:15:16 2021 +0000

    [otbn] Add URND/RND details to documentation
    
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
