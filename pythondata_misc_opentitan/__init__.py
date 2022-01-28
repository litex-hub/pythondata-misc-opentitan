import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9852"
version_tuple = (0, 0, 9852)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9852")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9728"
data_version_tuple = (0, 0, 9728)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9728")
except ImportError:
    pass
data_git_hash = "eadfa1b1fb98dd4dc094439cd3b8283e125d7002"
data_git_describe = "v0.0-9728-geadfa1b1f"
data_git_msg = """\
commit eadfa1b1fb98dd4dc094439cd3b8283e125d7002
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jan 25 21:50:12 2022 -0800

    [dv/hmac] Add wipe secret checking
    
    This PR adds a sequence to check the wipe secret functionality.
    The sequence will randomly issue wipe secret in the following four
    conditions:
    1). Before hmac key was input.
    2). Before hmac start command.
    3). Before hmac process command.
    4). Before hmac process is done.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
