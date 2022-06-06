import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12504"
version_tuple = (0, 0, 12504)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12504")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12362"
data_version_tuple = (0, 0, 12362)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12362")
except ImportError:
    pass
data_git_hash = "b0b81e6f2ba2176a8492125b41be8bdca222d7e7"
data_git_describe = "v0.0-12362-gb0b81e6f2"
data_git_msg = """\
commit b0b81e6f2ba2176a8492125b41be8bdca222d7e7
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Jun 1 14:07:33 2022 -0700

    [rust] Add rust analyzer target
    
    Generate a local `rust-project.json` with:
    ```
    bazel run //:gen_rust_project
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
