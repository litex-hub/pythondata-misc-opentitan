import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5464"
version_tuple = (0, 0, 5464)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5464")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5369"
data_version_tuple = (0, 0, 5369)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5369")
except ImportError:
    pass
data_git_hash = "d0ca7e97ffd988d9d9ec27a73d876ff009b29b79"
data_git_describe = "v0.0-5369-gd0ca7e97f"
data_git_msg = """\
commit d0ca7e97ffd988d9d9ec27a73d876ff009b29b79
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 15 13:00:32 2021 +0000

    [ci] Be more informative if install-package-dependencies fails
    
    Also, use a temporary directory to avoid polluting the checkout and
    move the logic to a shell script (no real change from the yaml file,
    but this script has got big enough that it doesn't feel like it should
    be inlined any more).
    
    Splitting out into a shell script means a bit of extra work, because
    we have to pass Azure Pipeline variables through to the script. Use
    proper command line arguments, rather than environment variables, to
    make it a bit more obvious what's going on.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
