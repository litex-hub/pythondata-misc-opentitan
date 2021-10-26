import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8455"
version_tuple = (0, 0, 8455)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8455")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8343"
data_version_tuple = (0, 0, 8343)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8343")
except ImportError:
    pass
data_git_hash = "7857ffea4cb85a76bd820a41a721fb9ecb33ac70"
data_git_describe = "v0.0-8343-g7857ffea4"
data_git_msg = """\
commit 7857ffea4cb85a76bd820a41a721fb9ecb33ac70
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Oct 25 16:13:45 2021 +0200

    [aes/rtl] Cause lint errors if Sec parameters get non-default values
    
    We want to avoid that the features controlled by these parameters get
    accidentally enabled in the final design.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
