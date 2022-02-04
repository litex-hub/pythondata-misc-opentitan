import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10085"
version_tuple = (0, 0, 10085)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10085")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9961"
data_version_tuple = (0, 0, 9961)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9961")
except ImportError:
    pass
data_git_hash = "2d05e9fecdb379eae1a91ba11d8b3ff88002b546"
data_git_describe = "v0.0-9961-g2d05e9fec"
data_git_msg = """\
commit 2d05e9fecdb379eae1a91ba11d8b3ff88002b546
Author: Alexander Williams <awill@google.com>
Date:   Wed Feb 2 08:28:42 2022 -0800

    [usbdev] Fix OUT response timeout bug
    
    The timeout counter has some broken logic, as it can never go down to 0.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
