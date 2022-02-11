import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10245"
version_tuple = (0, 0, 10245)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10245")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10121"
data_version_tuple = (0, 0, 10121)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10121")
except ImportError:
    pass
data_git_hash = "ca221a00278b20c82d3d0ffa092a52782c1c0b0d"
data_git_describe = "v0.0-10121-gca221a002"
data_git_msg = """\
commit ca221a00278b20c82d3d0ffa092a52782c1c0b0d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Feb 10 10:21:48 2022 -0800

    [dv/kmac] Fix kmac TL integrity error failure
    
    When kmac TL integrity error triggers, kmac will lock its internal
    states and also lock `cfg_regwen` register. Because the `cfg_regwen` is
    a `ro` register, RAL model won't lock its lockable registers
    automatically.
    So I separate out a task in common sequence, and override it in
    kmac_common_seq to lock the lockable regs
    immediately after tl integrity error is triggered.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
