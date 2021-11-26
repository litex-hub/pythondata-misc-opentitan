import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8870"
version_tuple = (0, 0, 8870)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8870")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8758"
data_version_tuple = (0, 0, 8758)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8758")
except ImportError:
    pass
data_git_hash = "3a672eb36aee5942d0912a15d15055b1d21c33d6"
data_git_describe = "v0.0-8758-g3a672eb36"
data_git_msg = """\
commit 3a672eb36aee5942d0912a15d15055b1d21c33d6
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Nov 26 14:17:14 2021 +0000

    [otbn,dv] Bug-fix: First insn uses faulty URND
    
    The bug was happening when the first executed
    instruction tried to use URND. Since first step
    did not resulted with a change in _value it was
    generating a None assingment as a value.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
