import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5245"
version_tuple = (0, 0, 5245)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5245")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5154"
data_version_tuple = (0, 0, 5154)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5154")
except ImportError:
    pass
data_git_hash = "861f56c6de6508714e461ad583c7fff8034346e7"
data_git_describe = "v0.0-5154-g861f56c6d"
data_git_msg = """\
commit 861f56c6de6508714e461ad583c7fff8034346e7
Author: Udi Jonnalagadda <udij@google.com>
Date:   Wed Mar 3 21:25:26 2021 -0800

    [dv/sram] add multiple_keys test
    
    this PR is a follow-up to the smoke test PR, and adds the multiple_keys
    test as specified in the testlist.
    
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
