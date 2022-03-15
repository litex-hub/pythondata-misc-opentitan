import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10892"
version_tuple = (0, 0, 10892)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10892")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10766"
data_version_tuple = (0, 0, 10766)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10766")
except ImportError:
    pass
data_git_hash = "ef51081c8a8e39519287b17c1fadb2edd4c7b141"
data_git_describe = "v0.0-10766-gef51081c8"
data_git_msg = """\
commit ef51081c8a8e39519287b17c1fadb2edd4c7b141
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Mar 9 15:53:29 2022 +0000

    [otbn,dv] Refactor step method in ISS
    
    We now have a separate method per FSM state, which I think should make
    things a bit easier to follow.
    
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
