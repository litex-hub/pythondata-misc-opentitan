import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14616"
version_tuple = (0, 0, 14616)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14616")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14474"
data_version_tuple = (0, 0, 14474)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14474")
except ImportError:
    pass
data_git_hash = "8d806f0428199346851603832521419b49a69b25"
data_git_describe = "v0.0-14474-g8d806f0428"
data_git_msg = """\
commit 8d806f0428199346851603832521419b49a69b25
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Thu Oct 6 05:15:21 2022 +0000

    [flash_ctrl,dv] Coverage update
    
    This PR has following updates
     - Update testplans for v2s
     - Fix eviction cover point from vector to index
     - Move sampling point of fetch code cover group
     - Increase test runs of some tests
     - Update flash_ctrl_disable error condition to '!= true'
     - Add error injection to fetch code test.
    
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
