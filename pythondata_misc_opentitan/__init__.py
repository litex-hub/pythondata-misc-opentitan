import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8674"
version_tuple = (0, 0, 8674)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8674")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8562"
data_version_tuple = (0, 0, 8562)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8562")
except ImportError:
    pass
data_git_hash = "dc440e33b494229eb6cb7dbd7da5105c1bf87b93"
data_git_describe = "v0.0-8562-gdc440e33b"
data_git_msg = """\
commit dc440e33b494229eb6cb7dbd7da5105c1bf87b93
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Nov 10 12:15:33 2021 -0800

    [dv/prim_alert_receiver] Fix assertion that consumes large mem
    
    This PR fixes an assertion sequence with large unbounded delays that
    consumes large memory runtime.
    If I understand correctly, we do not need to wait every clock cycle in
    the init state for `init_trig_i` to change to True. We only need the
    condition that we are in the init state and `init_trig_i` changes from
    true to false, and in which we have an alert signal integrity error.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
