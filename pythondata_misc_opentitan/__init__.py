import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15174"
version_tuple = (0, 0, 15174)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15174")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15032"
data_version_tuple = (0, 0, 15032)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15032")
except ImportError:
    pass
data_git_hash = "940943a8efe9c6dba318dc3f86e36be2142b5465"
data_git_describe = "v0.0-15032-g940943a8ef"
data_git_msg = """\
commit 940943a8efe9c6dba318dc3f86e36be2142b5465
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Nov 2 10:33:04 2022 -0400

    [bazel/ci] Query for git_repository rule in bazel to keep them out of WORKSPACE
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
