import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12979"
version_tuple = (0, 0, 12979)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12979")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12837"
data_version_tuple = (0, 0, 12837)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12837")
except ImportError:
    pass
data_git_hash = "7db360958179f8d7e7358099ca7a7981eb41423c"
data_git_describe = "v0.0-12837-g7db3609581"
data_git_msg = """\
commit 7db360958179f8d7e7358099ca7a7981eb41423c
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Thu Jul 7 10:26:19 2022 +0100

    [test] Remove entropy_src initialization from unneeded tests
    
     Besides the OTB that uses de EDN1, any other IPs needs to reset the entropy src.
     By removing entropy initialization from the unecessary tests we save a few minutes in the nightly regression.
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
