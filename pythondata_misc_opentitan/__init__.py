import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5703"
version_tuple = (0, 0, 5703)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5703")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5608"
data_version_tuple = (0, 0, 5608)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5608")
except ImportError:
    pass
data_git_hash = "9c0ed3194f337e376aa2f130088f060f46498874"
data_git_describe = "v0.0-5608-g9c0ed3194"
data_git_msg = """\
commit 9c0ed3194f337e376aa2f130088f060f46498874
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Apr 1 14:58:35 2021 -0700

    [formal] Update readme
    
    This PR udpates README for OT formal to include connectivity test.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
