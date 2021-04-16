import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5904"
version_tuple = (0, 0, 5904)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5904")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5809"
data_version_tuple = (0, 0, 5809)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5809")
except ImportError:
    pass
data_git_hash = "207cce085604ae6cb3978b43611d1d31b4682e47"
data_git_describe = "v0.0-5809-g207cce085"
data_git_msg = """\
commit 207cce085604ae6cb3978b43611d1d31b4682e47
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Apr 16 14:00:22 2021 +0100

    [pwm,lint] Hush an unused signal warning for regen signal
    
    We're not actually using this signal yet, and there's a TODO saying
    that we intend to. Rename it to "unused_regen" to silence both
    linters' warnings about it.
    
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
