import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9567"
version_tuple = (0, 0, 9567)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9567")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9445"
data_version_tuple = (0, 0, 9445)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9445")
except ImportError:
    pass
data_git_hash = "53b9e7d8e3c616764c175a489d566bddb1e6a6d9"
data_git_describe = "v0.0-9445-g53b9e7d8e"
data_git_msg = """\
commit 53b9e7d8e3c616764c175a489d566bddb1e6a6d9
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Dec 14 18:31:26 2021 +0000

    [otbn,dv] Add functional coverage for fatal SW errs
    
    This is a little fiddly because observing it happening requires two TL
    reads. If we're struggling to hit these bins, we could improve the
    tracking in the coverage code so that we can see it in more ways (e.g.
    read FATAL_ALERT_CAUSE before ERR_BITS).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
