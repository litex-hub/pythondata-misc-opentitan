import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10438"
version_tuple = (0, 0, 10438)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10438")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10312"
data_version_tuple = (0, 0, 10312)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10312")
except ImportError:
    pass
data_git_hash = "92173aa54ac2fba4c68b2362eb0bf7b563b09cfb"
data_git_describe = "v0.0-10312-g92173aa54"
data_git_msg = """\
commit 92173aa54ac2fba4c68b2362eb0bf7b563b09cfb
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Feb 15 23:41:41 2022 -0800

    [bazel] Add signing rule to `opentitan_binary` macro
    
    `opentitan_binary` images must be signed in order to be launched by the
    mask ROM, and therefore, facilitate E2E mask ROM testing. This commit
    adds a rule to the `rules/opentitan.bzl` and an option to sign
    opentitan binaries.
    
    This addresses a task in #10864.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
