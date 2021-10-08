import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8178"
version_tuple = (0, 0, 8178)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8178")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8066"
data_version_tuple = (0, 0, 8066)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8066")
except ImportError:
    pass
data_git_hash = "b106151c112f62def7c9bba0234f0bdb6638afea"
data_git_describe = "v0.0-8066-gb106151c1"
data_git_msg = """\
commit b106151c112f62def7c9bba0234f0bdb6638afea
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Oct 8 09:48:48 2021 +0100

    [otbn] Update comment to describe generic functionality
    
    This fixes the wording of a comment to show that the function it
    documents works for any OTBN application, not just RSA.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
