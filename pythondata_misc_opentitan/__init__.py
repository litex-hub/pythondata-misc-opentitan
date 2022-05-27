import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12378"
version_tuple = (0, 0, 12378)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12378")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12238"
data_version_tuple = (0, 0, 12238)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12238")
except ImportError:
    pass
data_git_hash = "5f50174370b6ffdca2f9c77a6e66ff40a370c9d6"
data_git_describe = "v0.0-12238-g5f5017437"
data_git_msg = """\
commit 5f50174370b6ffdca2f9c77a6e66ff40a370c9d6
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu May 26 15:40:40 2022 +0100

    [otbn,dv] Adjust assertions in otbn_rnd_if to handle ignored values
    
    The changes made in the RTL in 8e97525 and the documentation in
    46e134f allow a situation where data comes in from the EDN and is
    ignored.
    
    This commit tweaks the FSM diagram and associated assertions
    accordingly. I've also made signals for the transition labels to try
    to decouple the assertions and RTL signal names a little.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
