import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11435"
version_tuple = (0, 0, 11435)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11435")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11309"
data_version_tuple = (0, 0, 11309)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11309")
except ImportError:
    pass
data_git_hash = "8339519c379ad270bd2a091522ec564b08ebc41e"
data_git_describe = "v0.0-11309-g8339519c3"
data_git_msg = """\
commit 8339519c379ad270bd2a091522ec564b08ebc41e
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Apr 7 10:45:05 2022 +0100

    [python] Bump fusesoc/edalize versions
    
    These don't really introduce new functionality. The ot-0.2 release of
    fusesoc is essentially the same as ot-0.1, but rebased onto a more
    recent upstream fusesoc release.
    
    The ot-0.2 edalize tag points at a recent upstream version plus a
    minor bugfix that we need (which we'll try to upstream soon).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
