import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14365"
version_tuple = (0, 0, 14365)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14365")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14223"
data_version_tuple = (0, 0, 14223)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14223")
except ImportError:
    pass
data_git_hash = "d7415674079c483a85503bb266d10bfe1339008b"
data_git_describe = "v0.0-14223-gd741567407"
data_git_msg = """\
commit d7415674079c483a85503bb266d10bfe1339008b
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon Sep 19 19:20:45 2022 +0000

    [pwrmgr,dv] Add more test to stretch coverage
    
    - Add disable_rom_integrity_check test #11773
    - Add all states to invalid_state test to improve fsm coverage
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
