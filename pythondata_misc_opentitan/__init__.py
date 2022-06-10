import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12627"
version_tuple = (0, 0, 12627)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12627")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12485"
data_version_tuple = (0, 0, 12485)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12485")
except ImportError:
    pass
data_git_hash = "058344a4fc2a27460060718315407f4675fd5f00"
data_git_describe = "v0.0-12485-g058344a4f"
data_git_msg = """\
commit 058344a4fc2a27460060718315407f4675fd5f00
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Jun 9 18:31:03 2022 +0200

    [otbn] Extend description of CTRL.REDUN countermeasure label
    
    In addition to the actual blanking signals, this countermeasure now
    also covers control signals for the call stack, loop, branch/jump
    instructions and the branch target.
    
    This is related to lowRISC/OpenTitan#12768.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
