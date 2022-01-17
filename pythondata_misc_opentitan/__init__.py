import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9564"
version_tuple = (0, 0, 9564)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9564")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9442"
data_version_tuple = (0, 0, 9442)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9442")
except ImportError:
    pass
data_git_hash = "8c1c899c57a7479ab637f2b2c00fb4ccc03a2928"
data_git_describe = "v0.0-9442-g8c1c899c5"
data_git_msg = """\
commit 8c1c899c57a7479ab637f2b2c00fb4ccc03a2928
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Dec 16 16:55:55 2021 +0000

    [otbn,dv,doc] Add note in fcov.md about LC escalation tracking
    
    This is mainly for completeness so that someone reading through the
    document who thinks "Hey, what about life-cycle escalation signals?"
    can find the answer easily.
    
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
