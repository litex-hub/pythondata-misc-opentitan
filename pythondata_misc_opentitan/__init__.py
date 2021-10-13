import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8251"
version_tuple = (0, 0, 8251)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8251")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8139"
data_version_tuple = (0, 0, 8139)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8139")
except ImportError:
    pass
data_git_hash = "158a22b3aa48d579db1aded266d77e69609a4e4c"
data_git_describe = "v0.0-8139-g158a22b3a"
data_git_msg = """\
commit 158a22b3aa48d579db1aded266d77e69609a4e4c
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Oct 13 00:37:52 2021 -0700

    [util, dvsim] Remove CLOUDSDK_PYTHON override
    
    This override of Python version to invoke `gsutil` is no longer needed.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
