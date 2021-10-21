import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8364"
version_tuple = (0, 0, 8364)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8364")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8252"
data_version_tuple = (0, 0, 8252)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8252")
except ImportError:
    pass
data_git_hash = "20c2a9d955739eb101650d38be12207c4809eb46"
data_git_describe = "v0.0-8252-g20c2a9d95"
data_git_msg = """\
commit 20c2a9d955739eb101650d38be12207c4809eb46
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Oct 20 11:22:23 2021 -0700

    [doc/alert_handler] update register naming
    
    This PR fixes some register namings in alert_handler so the doc can link
    to the correct register.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
