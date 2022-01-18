import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9575"
version_tuple = (0, 0, 9575)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9575")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9453"
data_version_tuple = (0, 0, 9453)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9453")
except ImportError:
    pass
data_git_hash = "c26986551a1fd0f357e8a9ebcd739a7a64c27635"
data_git_describe = "v0.0-9453-gc26986551"
data_git_msg = """\
commit c26986551a1fd0f357e8a9ebcd739a7a64c27635
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Jan 18 09:22:40 2022 +0000

    [otbn,dv] Don't bother resetting at the end of err vseqs
    
    We'll handle this in any sequence that chains them together. This way,
    we can use one of these sequences if we want a locked OTBN for some
    reason.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
