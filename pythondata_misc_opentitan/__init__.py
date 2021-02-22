import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5088"
version_tuple = (0, 0, 5088)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5088")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4997"
data_version_tuple = (0, 0, 4997)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4997")
except ImportError:
    pass
data_git_hash = "b4142bc72027cf42767e14231abb336707cf960c"
data_git_describe = "v0.0-4997-gb4142bc72"
data_git_msg = """\
commit b4142bc72027cf42767e14231abb336707cf960c
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Feb 19 17:21:23 2021 +0000

    [otbn] Improve documentation for the Operations sections
    
    Also get rid of the pseudo-code notes at the end: this related to a
    version of the instruction set simulator from last summer; a lot has
    changed since then!
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
