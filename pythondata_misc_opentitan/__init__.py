import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11168"
version_tuple = (0, 0, 11168)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11168")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11042"
data_version_tuple = (0, 0, 11042)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11042")
except ImportError:
    pass
data_git_hash = "c2995063d22faaaf02b2054bc689a272a2499390"
data_git_describe = "v0.0-11042-gc2995063d"
data_git_msg = """\
commit c2995063d22faaaf02b2054bc689a272a2499390
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Mar 28 18:29:11 2022 -0700

    Revert "[aes] Fix clearing of data input registers"
    
    This reverts commit 8d507ad3f9dc47705b292a8e9568f73b772976ed.
    
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
