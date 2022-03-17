import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10941"
version_tuple = (0, 0, 10941)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10941")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10815"
data_version_tuple = (0, 0, 10815)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10815")
except ImportError:
    pass
data_git_hash = "fd0df25d021a94d23436f142b67f1ee2a4fcf0b7"
data_git_describe = "v0.0-10815-gfd0df25d0"
data_git_msg = """\
commit fd0df25d021a94d23436f142b67f1ee2a4fcf0b7
Author: Weicai Yang <weicai@google.com>
Date:   Wed Mar 16 22:54:01 2022 -0700

    [dv] Enable tlul_assert for CSR tests
    
    Some assert coverage can be only covered in CSR tests, such as b2b same
    address request.
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
