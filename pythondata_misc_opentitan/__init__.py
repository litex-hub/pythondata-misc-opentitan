import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9341"
version_tuple = (0, 0, 9341)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9341")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9224"
data_version_tuple = (0, 0, 9224)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9224")
except ImportError:
    pass
data_git_hash = "037e7f9a9c368e181df96fb31662ba37cc9d968b"
data_git_describe = "v0.0-9224-g037e7f9a9"
data_git_msg = """\
commit 037e7f9a9c368e181df96fb31662ba37cc9d968b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Jan 5 15:53:11 2022 +0000

    [chip,dv] Fix compilation for private CI
    
    This code come from PR 9740 (commit c1cf4a8), which needed updating
    for commit 28b1ab1451, merged in the meantime.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
