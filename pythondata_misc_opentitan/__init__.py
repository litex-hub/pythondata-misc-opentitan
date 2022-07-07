import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12969"
version_tuple = (0, 0, 12969)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12969")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12827"
data_version_tuple = (0, 0, 12827)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12827")
except ImportError:
    pass
data_git_hash = "525ce94fde59b87509d7e92493078b30e315770a"
data_git_describe = "v0.0-12827-g525ce94fde"
data_git_msg = """\
commit 525ce94fde59b87509d7e92493078b30e315770a
Author: Dan McArdle <dmcardle@google.com>
Date:   Thu Jun 30 12:33:59 2022 -0400

    [.github] Add advice to ignore unknown user errors
    
    See issue #13469
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
