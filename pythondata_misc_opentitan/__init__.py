import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10567"
version_tuple = (0, 0, 10567)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10567")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10441"
data_version_tuple = (0, 0, 10441)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10441")
except ImportError:
    pass
data_git_hash = "f5d229f75cff57803fe1dd445528317257527f2c"
data_git_describe = "v0.0-10441-gf5d229f75"
data_git_msg = """\
commit f5d229f75cff57803fe1dd445528317257527f2c
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Feb 25 15:03:47 2022 +0000

    [dv,top,pwm] Add initial place holder for pwm test
    
    add a new c test and sequence for pwm test.
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
