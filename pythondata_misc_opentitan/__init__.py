import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5196"
version_tuple = (0, 0, 5196)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5196")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5105"
data_version_tuple = (0, 0, 5105)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5105")
except ImportError:
    pass
data_git_hash = "e58e9732afde9c1abfbeea4f082b83f019d9a487"
data_git_describe = "v0.0-5105-ge58e9732a"
data_git_msg = """\
commit e58e9732afde9c1abfbeea4f082b83f019d9a487
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 2 09:31:21 2021 +0000

    [tlul] Fix "unused" name for AscentLint too
    
    It seems that Verilator is happy to treat foo_unused as a hint that
    the signal is unused, but AscentLint requires the name to start with
    unused instead.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
