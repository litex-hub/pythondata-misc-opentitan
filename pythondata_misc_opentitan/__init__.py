import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5855"
version_tuple = (0, 0, 5855)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5855")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5760"
data_version_tuple = (0, 0, 5760)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5760")
except ImportError:
    pass
data_git_hash = "fa9fc4d120c974e8ebfbcee435120afed4ba4b91"
data_git_describe = "v0.0-5760-gfa9fc4d12"
data_git_msg = """\
commit fa9fc4d120c974e8ebfbcee435120afed4ba4b91
Author: Udi Jonnalagadda <udij@google.com>
Date:   Tue Apr 13 14:39:02 2021 -0700

    [dv/kmac] fix kmac_smoke nightly failures
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
