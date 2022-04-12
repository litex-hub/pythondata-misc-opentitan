import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11517"
version_tuple = (0, 0, 11517)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11517")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11391"
data_version_tuple = (0, 0, 11391)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11391")
except ImportError:
    pass
data_git_hash = "6f50d51c9bcce79134834f569c7983777ce5f3c1"
data_git_describe = "v0.0-11391-g6f50d51c9"
data_git_msg = """\
commit 6f50d51c9bcce79134834f569c7983777ce5f3c1
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Apr 11 17:01:48 2022 +0100

    [rom_ctrl,dv] Wait for the right time before predicting an alert
    
    Doing it this way means that the wait time doesn't include all the
    time we spend sending data to KMAC. As such, we can use the default (7
    cycle) delay.
    
    No functional change, but failing tests will fail much quicker, rather
    than having to simulate several milliseconds of run time before
    deciding something went wrong.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
