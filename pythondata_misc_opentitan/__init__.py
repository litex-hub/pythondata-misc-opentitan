import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5572"
version_tuple = (0, 0, 5572)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5572")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5477"
data_version_tuple = (0, 0, 5477)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5477")
except ImportError:
    pass
data_git_hash = "1676b1b9ead14fab4463977a9c2132a00fc7f8ec"
data_git_describe = "v0.0-5477-g1676b1b9e"
data_git_msg = """\
commit 1676b1b9ead14fab4463977a9c2132a00fc7f8ec
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 19 14:50:50 2021 +0000

    [otbn] Track the operation of the idle_o interface
    
    This is possible in the scoreboard, but it's probably easier to just
    model with an FSM. Apart from anything else, getting the DONE signal
    out with a proper monitor would be rather difficult.
    
    Note that this commit slightly changes the behaviour of idle_o,
    removing a combinatorial path from the TL input to idle_o. There
    doesn't seem to be any need for it, and it makes the behaviour
    slightly easier to describe.
    
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
