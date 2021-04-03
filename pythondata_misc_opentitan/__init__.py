import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5707"
version_tuple = (0, 0, 5707)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5707")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5612"
data_version_tuple = (0, 0, 5612)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5612")
except ImportError:
    pass
data_git_hash = "4c519c5563c3da902c7170b46b119a054bc0ac80"
data_git_describe = "v0.0-5612-g4c519c556"
data_git_msg = """\
commit 4c519c5563c3da902c7170b46b119a054bc0ac80
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Apr 2 09:39:12 2021 -0700

    [sw/dif] Fix dif_hmac.h clang-format
    
    Also small compile fixes to dif_hmac_smoketest.c
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
