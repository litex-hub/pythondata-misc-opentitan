import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14223"
version_tuple = (0, 0, 14223)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14223")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14081"
data_version_tuple = (0, 0, 14081)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14081")
except ImportError:
    pass
data_git_hash = "4ba47bb4622ae5e9331f658d383002e806bdd51e"
data_git_describe = "v0.0-14081-g4ba47bb462"
data_git_msg = """\
commit 4ba47bb4622ae5e9331f658d383002e806bdd51e
Author: Jacob Levy <jacob.levy@nuvoton.com>
Date:   Mon Sep 12 14:15:54 2022 +0300

    [ast] Update the useability of the Jitter model
    
    Signed-off-by: Jacob Levy <jacob.levy@nuvoton.com>

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
