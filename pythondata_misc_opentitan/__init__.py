import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5506"
version_tuple = (0, 0, 5506)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5506")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5411"
data_version_tuple = (0, 0, 5411)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5411")
except ImportError:
    pass
data_git_hash = "0f218e98373626f382511c32bade43bf79596c3b"
data_git_describe = "v0.0-5411-g0f218e983"
data_git_msg = """\
commit 0f218e98373626f382511c32bade43bf79596c3b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 19 17:30:39 2021 +0000

    [prim_prince] Annotate some arrays to avoid UNOPTFLAT warnings
    
    Verilator's block scheduler isn't particularly clever, and it needs a
    bit of hand-holding when you have an array which updates like this:
    
        foo[0] = 123;
        foo[1] = f(foo[0]);
    
    Without the help, it sees foo depending on itself, which triggers an
    UNOPTFLAT warning (and slow simulation!)
    
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
