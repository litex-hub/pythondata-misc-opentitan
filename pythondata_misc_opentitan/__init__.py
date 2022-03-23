import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11029"
version_tuple = (0, 0, 11029)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11029")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10903"
data_version_tuple = (0, 0, 10903)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10903")
except ImportError:
    pass
data_git_hash = "356c0543eec55b5b583592329ffa787612d06830"
data_git_describe = "v0.0-10903-g356c0543e"
data_git_msg = """\
commit 356c0543eec55b5b583592329ffa787612d06830
Author: Cindy Liu <hcindyl@google.com>
Date:   Mon Mar 21 16:57:49 2022 -0700

    [topgen] Remove hard-code top name from topgen templates
    
    Retrieve the top name from the config dictionary.
    
    top level meson.build only has top_earlgrey defined. Leave top_earlgrey
    in SW device unit test meson.build.tpl for now since the build system
    goiing to be moved to bazel soon and this file will be deprecated
    afterwards.
    
    Signed-off-by: Cindy Liu <hcindyl@google.com>

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
