import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10396"
version_tuple = (0, 0, 10396)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10396")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10270"
data_version_tuple = (0, 0, 10270)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10270")
except ImportError:
    pass
data_git_hash = "4809deffb9cfbd4c326ad534375571c001144593"
data_git_describe = "v0.0-10270-g4809deffb"
data_git_msg = """\
commit 4809deffb9cfbd4c326ad534375571c001144593
Author: Jade Philipoom <jadep@google.com>
Date:   Thu Feb 10 10:39:04 2022 +0000

    [sw/silicon_creator] Use GlobalMock from device/lib.
    
    Remove now-duplicate GlobalMock from silicon_creator and change all
    mocks and tests to use it from its new location in
    device/lib/base/testing.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
