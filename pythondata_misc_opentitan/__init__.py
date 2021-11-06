import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8622"
version_tuple = (0, 0, 8622)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8622")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8510"
data_version_tuple = (0, 0, 8510)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8510")
except ImportError:
    pass
data_git_hash = "c26089ae313a0627c44ef77c4ad0e3f35f213a87"
data_git_describe = "v0.0-8510-gc26089ae3"
data_git_msg = """\
commit c26089ae313a0627c44ef77c4ad0e3f35f213a87
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Tue Nov 2 13:32:28 2021 -0700

    [csrng/rtl] sw port data attack check added
    
    For the software port only, the returned genbits will have a repeated data check before genbits are returned to the register interface.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
