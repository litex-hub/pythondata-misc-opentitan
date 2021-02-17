import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5019"
version_tuple = (0, 0, 5019)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5019")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4928"
data_version_tuple = (0, 0, 4928)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4928")
except ImportError:
    pass
data_git_hash = "ff3cce2a482cfe82cdf63d25271bfbd44ea58253"
data_git_describe = "v0.0-4928-gff3cce2a4"
data_git_msg = """\
commit ff3cce2a482cfe82cdf63d25271bfbd44ea58253
Author: Udi Jonnalagadda <udij@google.com>
Date:   Thu Feb 11 23:19:42 2021 -0800

    [dv/kmac] randomly read digest after hashing
    
    This PR adds functionality for the test sequence to randomly read out
    the state digest after finishing a hash, to check that the digest is no
    longer readable.
    
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
