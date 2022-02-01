import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9977"
version_tuple = (0, 0, 9977)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9977")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9853"
data_version_tuple = (0, 0, 9853)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9853")
except ImportError:
    pass
data_git_hash = "3f7ec1a83a806ddab8ffe655fe40556467929eb5"
data_git_describe = "v0.0-9853-g3f7ec1a83"
data_git_msg = """\
commit 3f7ec1a83a806ddab8ffe655fe40556467929eb5
Author: Drew Macrae <drewmacrae@google.com>
Date:   Fri Jan 28 17:14:18 2022 -0800

    [bazel] Add a quick-bazel script to rerun CI
    
    Script is added and used by azure-pipelines.yml
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
