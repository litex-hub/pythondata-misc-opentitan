import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8540"
version_tuple = (0, 0, 8540)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8540")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8428"
data_version_tuple = (0, 0, 8428)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8428")
except ImportError:
    pass
data_git_hash = "258511537aa2df03daf36fbe1c0c5b7dca5e3fa6"
data_git_describe = "v0.0-8428-g258511537"
data_git_msg = """\
commit 258511537aa2df03daf36fbe1c0c5b7dca5e3fa6
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Oct 29 16:54:54 2021 +0100

    [otbn,dv] Run Python model with -u
    
    This disables buffering at the block level for stdout and stderr in
    the Python subprocess. Without this argument, it seems that Python
    3.6, at least, buffers sys.stderr at the block level if it doesn't
    point at a console. When run under dvsim, it points at the run.log
    file.
    
    With this fixed, you can add debug prints to the model with something
    like
    
        print('my message', file=sys.stderr)
    
    and have it appear in the log output. Without the flag, you need to
    follow with a sys.stderr.flush() to be sure to see the result.
    
    This isn't a problem with recent versions of Python: it seems that
    they changed the default behaviour at some point.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
