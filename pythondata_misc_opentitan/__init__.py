import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8957"
version_tuple = (0, 0, 8957)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8957")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8845"
data_version_tuple = (0, 0, 8845)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8845")
except ImportError:
    pass
data_git_hash = "c1bd139dc158a06af943b4f93130a9ffeccc381e"
data_git_describe = "v0.0-8845-gc1bd139dc"
data_git_msg = """\
commit c1bd139dc158a06af943b4f93130a9ffeccc381e
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Dec 1 17:42:09 2021 +0000

    [bazel] add entries for bazel to CODEOWNERS
    
    Assign codeownership for
    * BUILD
    * WORKSPACE
    * *.bzl
    * .bazelrc
    files to drewmacrae and cfrantz to help automate reviewing.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
