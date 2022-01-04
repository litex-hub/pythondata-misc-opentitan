import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9312"
version_tuple = (0, 0, 9312)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9312")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9195"
data_version_tuple = (0, 0, 9195)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9195")
except ImportError:
    pass
data_git_hash = "a510f8e1f1ae7efd0f6924d376cea58295f2ce3b"
data_git_describe = "v0.0-9195-ga510f8e1f"
data_git_msg = """\
commit a510f8e1f1ae7efd0f6924d376cea58295f2ce3b
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Dec 7 09:45:55 2021 +0000

    [sw] Fix endianness bit in HMAC DIF.
    
    According to the HMAC block specification, the digest is big-endian when
    the `digest_swap` bit is 1, and little-endian if it's 0; the DIF had
    these switched.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
