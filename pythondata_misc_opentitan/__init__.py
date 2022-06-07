import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12542"
version_tuple = (0, 0, 12542)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12542")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12400"
data_version_tuple = (0, 0, 12400)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12400")
except ImportError:
    pass
data_git_hash = "8a464dc6979d2dcb8f2cca9bb02e195e0489889e"
data_git_describe = "v0.0-12400-g8a464dc69"
data_git_msg = """\
commit 8a464dc6979d2dcb8f2cca9bb02e195e0489889e
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Jun 2 19:18:28 2022 -0700

    [bazel] further enhance manufacturer test hooks repo setup
    
    This further enhances the manufacturer test hooks bazel repository to:
    
    1. support writing multiple sets of test hooks in the same
       MANUFACTURER_HOOKS_DIR,
    2. support toggling between which test hooks are enabled via a bazel
       command line switch, e.g., `--define test_hooks=<hooks library>`,
    3. support writing multiple closed source `opentitan_functest` tests in
       the same MANUFACTURER_HOOKS_DIR as the test hooks, and
    4. updating the `README.md` and `BUILD.bazel` comments with detailed
       instructions on how extend these features.
    
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
