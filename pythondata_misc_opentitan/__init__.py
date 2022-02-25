import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10541"
version_tuple = (0, 0, 10541)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10541")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10415"
data_version_tuple = (0, 0, 10415)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10415")
except ImportError:
    pass
data_git_hash = "a3defd07c170d5e2841b899933b8e4676bf9d4ec"
data_git_describe = "v0.0-10415-ga3defd07c"
data_git_msg = """\
commit a3defd07c170d5e2841b899933b8e4676bf9d4ec
Author: Michael Tempelmeier <michael.tempelmeier@gi-de.com>
Date:   Tue Feb 15 11:26:48 2022 +0100

    [kmac] declared CTR.REDUN for key index and sentmsg_count
    
    Signed-off-by: Michael Tempelmeier <michael.tempelmeier@gi-de.com>

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
