import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10950"
version_tuple = (0, 0, 10950)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10950")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10824"
data_version_tuple = (0, 0, 10824)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10824")
except ImportError:
    pass
data_git_hash = "019c184896f5b7f7c8e30751f67745ba6267e566"
data_git_describe = "v0.0-10824-g019c18489"
data_git_msg = """\
commit 019c184896f5b7f7c8e30751f67745ba6267e566
Author: Alexander Williams <awill@google.com>
Date:   Wed Mar 16 09:05:52 2022 -0700

    [usbdev] Update checklist for reaching D2S
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
