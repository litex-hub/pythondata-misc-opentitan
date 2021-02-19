import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5045"
version_tuple = (0, 0, 5045)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5045")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4954"
data_version_tuple = (0, 0, 4954)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4954")
except ImportError:
    pass
data_git_hash = "f67df357341da37297ba1feba5fa02f7811d119d"
data_git_describe = "v0.0-4954-gf67df3573"
data_git_msg = """\
commit f67df357341da37297ba1feba5fa02f7811d119d
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Feb 18 13:12:46 2021 -0800

    [kmac] Latch absorbed signal to delay Done command
    
    kmac_keymgr interface asserts `CmdDone` when it sees `absorbed` signal.
    The SHA3 module asserts absorbed signal when it is in `StAbsorb` but the
    next state is `StSqueeze`. It creates assertion error as only
    `StSqueeze` expects `CmdDone`.
    
    To break the timing path, latch in absorbed_o is added.
    
    This issue is reported by @udinator
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
