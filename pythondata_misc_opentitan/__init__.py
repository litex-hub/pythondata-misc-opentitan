import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5071"
version_tuple = (0, 0, 5071)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5071")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4980"
data_version_tuple = (0, 0, 4980)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4980")
except ImportError:
    pass
data_git_hash = "22b9f11bfb610654c76b2d42c17d0f7a662b8b27"
data_git_describe = "v0.0-4980-g22b9f11bf"
data_git_msg = """\
commit 22b9f11bfb610654c76b2d42c17d0f7a662b8b27
Author: Udi Jonnalagadda <udij@google.com>
Date:   Thu Feb 18 19:55:27 2021 -0800

    [dv/kmac] reduce length of long_msg test
    
    this PR reduces the input message size to reduce the runtime of the
    `long_msg_and_output` test in nightly regressions.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
