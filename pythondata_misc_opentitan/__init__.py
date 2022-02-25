import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10554"
version_tuple = (0, 0, 10554)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10554")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10428"
data_version_tuple = (0, 0, 10428)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10428")
except ImportError:
    pass
data_git_hash = "6497101e7a591c70c535822e09f8e324cea97455"
data_git_describe = "v0.0-10428-g6497101e7"
data_git_msg = """\
commit 6497101e7a591c70c535822e09f8e324cea97455
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Feb 11 09:47:00 2022 -0800

    [doc/flash_crtl] Fix some of the wording
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
