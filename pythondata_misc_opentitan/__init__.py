import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12664"
version_tuple = (0, 0, 12664)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12664")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12522"
data_version_tuple = (0, 0, 12522)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12522")
except ImportError:
    pass
data_git_hash = "f14a76a191a759754ad3519699ff922ed2e185c3"
data_git_describe = "v0.0-12522-gf14a76a19"
data_git_msg = """\
commit f14a76a191a759754ad3519699ff922ed2e185c3
Author: Miles Dai <milesdai@google.com>
Date:   Wed Jun 8 12:31:03 2022 -0400

    [ci] Retry install-package-dependencies up to 3 times on failure
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
