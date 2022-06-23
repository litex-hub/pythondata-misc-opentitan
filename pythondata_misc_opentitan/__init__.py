import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12816"
version_tuple = (0, 0, 12816)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12816")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12674"
data_version_tuple = (0, 0, 12674)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12674")
except ImportError:
    pass
data_git_hash = "c6f17697b223ea7db872e0d62115a9e937e2fbd4"
data_git_describe = "v0.0-12674-gc6f17697b2"
data_git_msg = """\
commit c6f17697b223ea7db872e0d62115a9e937e2fbd4
Author: Dan McArdle <dmcardle@google.com>
Date:   Wed Jun 22 14:53:42 2022 -0400

    [util] Add util/generate_compilation_db.py
    
    This script generates compile_commands.json.
    
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
