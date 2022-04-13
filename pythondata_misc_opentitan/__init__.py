import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11560"
version_tuple = (0, 0, 11560)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11560")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11434"
data_version_tuple = (0, 0, 11434)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11434")
except ImportError:
    pass
data_git_hash = "9ab6a2dcb4005a3dcf15c65022377e1646238b13"
data_git_describe = "v0.0-11434-g9ab6a2dcb"
data_git_msg = """\
commit 9ab6a2dcb4005a3dcf15c65022377e1646238b13
Author: Alexander Williams <awill@google.com>
Date:   Fri Apr 8 07:51:09 2022 -0700

    [pinmux/dif] Update checklist for usage and unit tests
    
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
