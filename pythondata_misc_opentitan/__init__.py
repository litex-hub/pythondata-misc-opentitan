import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11193"
version_tuple = (0, 0, 11193)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11193")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11067"
data_version_tuple = (0, 0, 11067)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11067")
except ImportError:
    pass
data_git_hash = "1a55cd2440a21ca7bb117a0814054891a1f76a48"
data_git_describe = "v0.0-11067-g1a55cd244"
data_git_msg = """\
commit 1a55cd2440a21ca7bb117a0814054891a1f76a48
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 21 21:00:29 2022 +0000

    [otbn,dv] Fix confusingly named "top_addr" in RIG's known_mem.py
    
    The "top address" in this code isn't actually the top address: it's
    the number afterwards! Rename to "size_bytes" to make things a bit
    less confusing.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
