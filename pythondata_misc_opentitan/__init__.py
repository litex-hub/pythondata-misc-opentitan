import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12265"
version_tuple = (0, 0, 12265)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12265")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12137"
data_version_tuple = (0, 0, 12137)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12137")
except ImportError:
    pass
data_git_hash = "421b9a95536da34e9efcc5b84ec6fbd555e02e39"
data_git_describe = "v0.0-12137-g421b9a955"
data_git_msg = """\
commit 421b9a95536da34e9efcc5b84ec6fbd555e02e39
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri May 20 12:15:58 2022 +0100

    [otbn,dv] Re-order definitions in otbn_model
    
    This is a little nitty, but the definitions in the header file, C++
    file and both DPI headers were all in different orders. And, in some
    cases, quite bizarre orders! Put them all the same way around.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
