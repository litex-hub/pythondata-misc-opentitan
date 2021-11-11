import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8676"
version_tuple = (0, 0, 8676)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8676")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8564"
data_version_tuple = (0, 0, 8564)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8564")
except ImportError:
    pass
data_git_hash = "8630bcbbb59325eea9a52e364ac1dfdce7804758"
data_git_describe = "v0.0-8564-g8630bcbbb"
data_git_msg = """\
commit 8630bcbbb59325eea9a52e364ac1dfdce7804758
Author: Jade Philipoom <jadep@google.com>
Date:   Wed Nov 10 13:24:16 2021 +0000

    [doc] Add OTBN style guide.
    
    Fixes #3314
    Fixes #3607
    
    Adds a starting point for an OTBN-specific assembly style guide based on
    existing OTBN code and discussions on previous issues.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
