import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8134"
version_tuple = (0, 0, 8134)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8134")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8029"
data_version_tuple = (0, 0, 8029)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8029")
except ImportError:
    pass
data_git_hash = "45cb5d38bc86d0147801dc3a81130ba29be4ad9c"
data_git_describe = "v0.0-8029-g45cb5d38b"
data_git_msg = """\
commit 45cb5d38bc86d0147801dc3a81130ba29be4ad9c
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Oct 5 18:23:33 2021 +0100

    [otbn] Disable writing to CTRL.software_errs_fatal in CSR tests
    
    Writes don't work currently as the field is unimplemented.
    
    Fixes #8525
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post105"
tool_version_tuple = (0, 0, 105)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post105")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
