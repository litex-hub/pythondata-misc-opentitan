import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10474"
version_tuple = (0, 0, 10474)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10474")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10348"
data_version_tuple = (0, 0, 10348)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10348")
except ImportError:
    pass
data_git_hash = "aa91c773d6a787c9776d51392ad6475dfad2bb6c"
data_git_describe = "v0.0-10348-gaa91c773d"
data_git_msg = """\
commit aa91c773d6a787c9776d51392ad6475dfad2bb6c
Author: Jon Flatley <jflat@google.com>
Date:   Wed Feb 16 17:00:27 2022 -0500

    [sw] Move rust version to 1.58.0
    
    Currently using rust 1.55.0 in CI and Docker, and it the version listed
    in the tool requirements. Bazel is currently building with rust 1.53.0.
    Move everything to use rust 1.58.0.
    
    Signed-off-by: Jon Flatley <jflat@google.com>

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
