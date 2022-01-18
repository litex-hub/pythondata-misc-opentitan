import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9580"
version_tuple = (0, 0, 9580)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9580")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9458"
data_version_tuple = (0, 0, 9458)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9458")
except ImportError:
    pass
data_git_hash = "51abd9f8d94d9a362c49b2de851ff17d6bee5d46"
data_git_describe = "v0.0-9458-g51abd9f8d"
data_git_msg = """\
commit 51abd9f8d94d9a362c49b2de851ff17d6bee5d46
Author: Drew Macrae <drewmacrae@google.com>
Date:   Tue Dec 7 14:54:24 2021 +0000

    [bazel] Docs ignore bazel's build directories
    
    Our site configs need another entry to ignore bazel build directories
    when building documentation.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
