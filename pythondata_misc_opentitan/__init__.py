import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12259"
version_tuple = (0, 0, 12259)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12259")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12131"
data_version_tuple = (0, 0, 12131)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12131")
except ImportError:
    pass
data_git_hash = "c5be2597f3b41dac1fd1a7354be46ff7c6704f05"
data_git_describe = "v0.0-12131-gc5be2597f"
data_git_msg = """\
commit c5be2597f3b41dac1fd1a7354be46ff7c6704f05
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri May 20 11:06:03 2022 +0100

    [otbn,dv] Remove unused rnd_req field
    
    This was added in 051133d, but isn't needed: that commit eventually
    switched to tracking the EDN request in a RND_REQ external register.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
