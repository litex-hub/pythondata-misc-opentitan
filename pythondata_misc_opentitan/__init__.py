import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8687"
version_tuple = (0, 0, 8687)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8687")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8575"
data_version_tuple = (0, 0, 8575)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8575")
except ImportError:
    pass
data_git_hash = "7ac1efb06d902d95595317c9ca68d8a80c6531dd"
data_git_describe = "v0.0-8575-g7ac1efb06"
data_git_msg = """\
commit 7ac1efb06d902d95595317c9ca68d8a80c6531dd
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Sep 22 16:08:28 2021 +0000

    [bazel] Rules for hello_world binary for riscv
    
    fixes to enable stricter builds:
    * ibex.h uses stdint, and should include it
    * ISO C does not allow extra semicolons
    
    use .bazelrc to keep bazel from running in a legacy mode
    add -std=c11 option for c compilation
    
    add and modify rules for bazel to build hello-world binary
    and it's dependencies
    
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
