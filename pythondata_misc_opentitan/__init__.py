import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15133"
version_tuple = (0, 0, 15133)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15133")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14991"
data_version_tuple = (0, 0, 14991)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14991")
except ImportError:
    pass
data_git_hash = "acfd5d07d1ccc5dce3a588ae67ba8ba4f0f2b4f3"
data_git_describe = "v0.0-14991-gacfd5d07d1"
data_git_msg = """\
commit acfd5d07d1ccc5dce3a588ae67ba8ba4f0f2b4f3
Author: Drew Macrae <drewmacrae@google.com>
Date:   Mon Oct 31 22:39:44 2022 -0400

    [bazel] Build verilated model with -j 4 by default
    
    CI should still be constrained where it's run on smaller VMs
    
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
