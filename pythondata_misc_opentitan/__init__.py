import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12726"
version_tuple = (0, 0, 12726)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12726")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12584"
data_version_tuple = (0, 0, 12584)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12584")
except ImportError:
    pass
data_git_hash = "c16937ec940832a450fba47bea6ea851c5448087"
data_git_describe = "v0.0-12584-gc16937ec9"
data_git_msg = """\
commit c16937ec940832a450fba47bea6ea851c5448087
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Jun 15 20:19:01 2022 -0700

    [lib,timing] Fix busy_spin_micros
    
    Improve the accuracy of the conversion from microseconds to cpu cycles.
    Use a per platform to_cpu_cycles function that doesn't use long division,
    or inaccurate approximations of it.
    
    Fixes #12889
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
