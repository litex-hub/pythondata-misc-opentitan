import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14620"
version_tuple = (0, 0, 14620)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14620")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14478"
data_version_tuple = (0, 0, 14478)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14478")
except ImportError:
    pass
data_git_hash = "4369d88a4223bc7fdd318e9d1686a70e0f327890"
data_git_describe = "v0.0-14478-g4369d88a42"
data_git_msg = """\
commit 4369d88a4223bc7fdd318e9d1686a70e0f327890
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Oct 6 15:29:21 2022 -0700

    [prim] Simplify defensive coding
    
    The previous code in this area was somewhat "conservative" and
    qualified the ack with the busy condition.  However, coverage
    tools were able to show that the inverse condition does not happen,
    so instead move the qualification to an assertion to simplify
    the coverage waivers.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
