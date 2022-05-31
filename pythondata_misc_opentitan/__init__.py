import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12420"
version_tuple = (0, 0, 12420)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12420")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12278"
data_version_tuple = (0, 0, 12278)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12278")
except ImportError:
    pass
data_git_hash = "25e8e9f8895a12daa361f5a7a1af20e05edf802a"
data_git_describe = "v0.0-12278-g25e8e9f88"
data_git_msg = """\
commit 25e8e9f8895a12daa361f5a7a1af20e05edf802a
Author: Michał Mazurek <maz@semihalf.com>
Date:   Thu Mar 31 17:10:53 2022 +0200

    [opentitanlib] Implementations of Emulator trait for Ti50Emulator
    
    This commit provides methods to control TockOS Host Emulation
    kernel process. Implementation use 'runtime' directory with will hold
    all state files used by Ti50Emulator sub-process during its lifetime.
    Files in this directory should not be directly modified by the user.
    Updating their content should be done by passing the appropriate
    arguments to the 'start' function.
    
    Signed-off-by: Michał Mazurek <maz@semihalf.com>

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
