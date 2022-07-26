import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13262"
version_tuple = (0, 0, 13262)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13262")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13120"
data_version_tuple = (0, 0, 13120)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13120")
except ImportError:
    pass
data_git_hash = "2f044ef0e564a055f1a0d639eb646fc7af7be606"
data_git_describe = "v0.0-13120-g2f044ef0e5"
data_git_msg = """\
commit 2f044ef0e564a055f1a0d639eb646fc7af7be606
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Jul 25 14:29:35 2022 -0700

    [dv/kmac] Fix EDN timeout assertion failures
    
    This PR fixes edn_timeout test's assertion failures:
    1). Req should be asserted until ack -> Fix this assertion error by
      extending the disable check statement to sequence level.
    2). Fix a path within the disable assertion statement in DV.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
