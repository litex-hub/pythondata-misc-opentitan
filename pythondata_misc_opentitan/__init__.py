import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15042"
version_tuple = (0, 0, 15042)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15042")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14900"
data_version_tuple = (0, 0, 14900)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14900")
except ImportError:
    pass
data_git_hash = "d2dce395b2128e5acc40fa772cfd565e4754c82a"
data_git_describe = "v0.0-14900-gd2dce395b2"
data_git_msg = """\
commit d2dce395b2128e5acc40fa772cfd565e4754c82a
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Oct 28 21:38:24 2022 -0700

    [bazel] rollback #15817 again
    
    This rolls back the rust toolchain update again as there seems to be an
    inconsistent environment between slightly different variations in our
    airgapped environment.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
