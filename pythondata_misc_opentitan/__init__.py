import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10314"
version_tuple = (0, 0, 10314)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10314")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10188"
data_version_tuple = (0, 0, 10188)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10188")
except ImportError:
    pass
data_git_hash = "10e82b8449dcdc700deb307c0c8fc6d30f69c8c0"
data_git_describe = "v0.0-10188-g10e82b844"
data_git_msg = """\
commit 10e82b8449dcdc700deb307c0c8fc6d30f69c8c0
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Feb 14 17:14:58 2022 -0800

    [dv/kmac] kmac key not valid case
    
    This PR separates the key not valid case from key_errors because it is
    quite complicate for scb to handle it.
    The following PR will clean up kmac scb and add this sequence to
    stress_all sequence list.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
