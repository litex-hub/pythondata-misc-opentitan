import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12579"
version_tuple = (0, 0, 12579)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12579")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12437"
data_version_tuple = (0, 0, 12437)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12437")
except ImportError:
    pass
data_git_hash = "e3835e82cc5c2632aba44ae2d9da9254b75b3ebb"
data_git_describe = "v0.0-12437-ge3835e82c"
data_git_msg = """\
commit e3835e82cc5c2632aba44ae2d9da9254b75b3ebb
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Jun 8 13:34:00 2022 -0400

    [cryptolib/hmac] Fix IRQ clearing in hmac_sha256_init()
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
