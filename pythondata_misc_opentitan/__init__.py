import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11449"
version_tuple = (0, 0, 11449)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11449")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11323"
data_version_tuple = (0, 0, 11323)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11323")
except ImportError:
    pass
data_git_hash = "6fa56cff07af3bcaad0a411bb4e47c09232d85f5"
data_git_describe = "v0.0-11323-g6fa56cff0"
data_git_msg = """\
commit 6fa56cff07af3bcaad0a411bb4e47c09232d85f5
Author: Weicai Yang <weicai@google.com>
Date:   Wed Apr 6 22:23:25 2022 -0700

    [top, dv] Fix bootstrap test
    
    It takes more time to process a frame of data, fixed TB sending SPI data
    too fast.
    Changed to wait for a message from SW to know the frame processed is
    done.
    
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
