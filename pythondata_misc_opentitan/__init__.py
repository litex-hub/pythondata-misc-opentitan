import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15044"
version_tuple = (0, 0, 15044)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15044")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14902"
data_version_tuple = (0, 0, 14902)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14902")
except ImportError:
    pass
data_git_hash = "811cd61fd9637a4c72c162c04fae707dc869970a"
data_git_describe = "v0.0-14902-g811cd61fd9"
data_git_msg = """\
commit 811cd61fd9637a4c72c162c04fae707dc869970a
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Oct 21 04:18:14 2022 +0000

    [chip,dv,flash_ctrl] Add flash crush escalation test
    
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
