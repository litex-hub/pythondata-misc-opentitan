import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13170"
version_tuple = (0, 0, 13170)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13170")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13028"
data_version_tuple = (0, 0, 13028)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13028")
except ImportError:
    pass
data_git_hash = "3a5e6ca8eb97fb99f824e3f37bd9a9b3c94b5bcc"
data_git_describe = "v0.0-13028-g3a5e6ca8eb"
data_git_msg = """\
commit 3a5e6ca8eb97fb99f824e3f37bd9a9b3c94b5bcc
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Mon Jul 18 15:48:04 2022 -0700

    feat(rdc): Define RDC gitattribute
    
    This commit defines RDC related files as CDC in `.gitattributes`.
    By defining as cdc, any changes to RDC skip the FPGA tests in CI.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
