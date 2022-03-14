import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10860"
version_tuple = (0, 0, 10860)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10860")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10734"
data_version_tuple = (0, 0, 10734)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10734")
except ImportError:
    pass
data_git_hash = "1891e9dc5a9bbbb1768ef494651d7881f9ce8087"
data_git_describe = "v0.0-10734-g1891e9dc5"
data_git_msg = """\
commit 1891e9dc5a9bbbb1768ef494651d7881f9ce8087
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 10 18:10:34 2022 -0800

    [keymgr] Changing fault wiping behavior
    
    - change key manager wiping from operation boundary aligned to immediate.
    - this addresses an item in #11387
    - this change causes keymgr to enter wiping state much earlier than usual.
    - the wiping stage outputs random data to kmac and causes a push-pull assertion failure.
    - disable the assertion in the test
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
