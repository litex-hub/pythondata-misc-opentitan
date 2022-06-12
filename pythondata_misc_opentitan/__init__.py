import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12652"
version_tuple = (0, 0, 12652)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12652")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12510"
data_version_tuple = (0, 0, 12510)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12510")
except ImportError:
    pass
data_git_hash = "b3a109385bd118a428a4e30d4336377ea88db5f9"
data_git_describe = "v0.0-12510-gb3a109385"
data_git_msg = """\
commit b3a109385bd118a428a4e30d4336377ea88db5f9
Author: Chris Frantz <cfrantz@google.com>
Date:   Fri Jun 3 14:52:06 2022 -0700

    [rust] Add a cargo raze rule
    
    Rather than remembering the proper bazel invocation of cargo_raze,
    add a rule that invokes it correctly with:
    
    ```
    bazel run //:cargo_raze
    ```
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
