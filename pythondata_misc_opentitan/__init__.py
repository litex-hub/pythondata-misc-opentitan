import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15149"
version_tuple = (0, 0, 15149)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15149")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15007"
data_version_tuple = (0, 0, 15007)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15007")
except ImportError:
    pass
data_git_hash = "b77dc2319ba57106c7617b7931326088405e951e"
data_git_describe = "v0.0-15007-gb77dc2319b"
data_git_msg = """\
commit b77dc2319ba57106c7617b7931326088405e951e
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon Oct 31 22:50:53 2022 +0000

    [flash_ctrl,dv] Sign off V2S
    
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
