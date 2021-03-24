import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5543"
version_tuple = (0, 0, 5543)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5543")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5448"
data_version_tuple = (0, 0, 5448)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5448")
except ImportError:
    pass
data_git_hash = "f2b7ef068d6414314c2f0f51ea73d8d1c339f1dd"
data_git_describe = "v0.0-5448-gf2b7ef068"
data_git_msg = """\
commit f2b7ef068d6414314c2f0f51ea73d8d1c339f1dd
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 22 11:19:10 2021 +0000

    [otbn] Add a "multi" vseq to run binaries back-to-back
    
    This should catch errors where we don't re-initialise enough of the
    design when starting a new operation. It intentionally doesn't do a
    reset, which would hide that sort of thing.
    
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
