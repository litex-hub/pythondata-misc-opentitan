import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14835"
version_tuple = (0, 0, 14835)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14835")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14693"
data_version_tuple = (0, 0, 14693)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14693")
except ImportError:
    pass
data_git_hash = "d120ffa33297e9e9b807388308076a5e6d40c4d1"
data_git_describe = "v0.0-14693-gd120ffa332"
data_git_msg = """\
commit d120ffa33297e9e9b807388308076a5e6d40c4d1
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 12 11:24:53 2022 -0700

    [bazel] update rules_rust to enable bindgen
    
    This updates rules_rust to fix #15441 and #15568, and enable using the rust
    bindgen tool in (older linux) airgapped environments.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
