import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12494"
version_tuple = (0, 0, 12494)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12494")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12352"
data_version_tuple = (0, 0, 12352)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12352")
except ImportError:
    pass
data_git_hash = "d2277d216b55f9d26373750f703f3050d617d8e7"
data_git_describe = "v0.0-12352-gd2277d216"
data_git_msg = """\
commit d2277d216b55f9d26373750f703f3050d617d8e7
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Jun 2 00:36:08 2022 -0700

    [bazel] update closed source example repo with custom test
    
    In #12631 Bazel infrastructure was added to support closed-source
    manufacture test hooks. This extends those capabilities by also enabling
    manufacturers to develop entire tests that are also closed source,
    inside the same external Bazel repository
    (`@manufacturer_test_hooks//`).
    
    Additionally, this commit adds an example closed source test. To build
    this test within the default closed-source bazel repo use:
    `bazel build @manufacturer_test_hooks//:example_test`
    
    To build a test in a closed-source test hooks repo that is located
    elsewhere on your machine, use:
    
    `MANUFACTURER_HOOKS_DIR=/path/to/test_hooks_dir bazel build
    @manufacturer_test_hooks//:example_test`
    
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
