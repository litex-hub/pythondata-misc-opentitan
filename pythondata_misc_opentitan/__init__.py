import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14118"
version_tuple = (0, 0, 14118)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14118")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13976"
data_version_tuple = (0, 0, 13976)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13976")
except ImportError:
    pass
data_git_hash = "91e674c39b045e5c85f17e0989cae1a719280bc7"
data_git_describe = "v0.0-13976-g91e674c39b"
data_git_msg = """\
commit 91e674c39b045e5c85f17e0989cae1a719280bc7
Author: Jade Philipoom <jadep@google.com>
Date:   Mon Aug 1 16:37:19 2022 +0100

    [silicon_creator] Ensure OTBN is idle before writes/commands.
    
    Adjust the silicon_creator OTBN driver to add a blocking check that OTBN
    is idle and call this before loading applciations. Since OTBN now
    performs a secure wipe after coming out of reset, this check is needed
    to ensure mask ROM code waits for the secure wipe to finish.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
