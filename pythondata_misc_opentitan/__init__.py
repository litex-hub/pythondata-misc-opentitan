import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10979"
version_tuple = (0, 0, 10979)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10979")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10853"
data_version_tuple = (0, 0, 10853)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10853")
except ImportError:
    pass
data_git_hash = "6d96cdf7819cfaf0a58638abe6eff21b651ed475"
data_git_describe = "v0.0-10853-g6d96cdf78"
data_git_msg = """\
commit 6d96cdf7819cfaf0a58638abe6eff21b651ed475
Author: Miles Dai <milesdai@google.com>
Date:   Wed Mar 9 18:45:49 2022 -0500

    [ci] Upload generated bitstream to public GCP bucket
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
