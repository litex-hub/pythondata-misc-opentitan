import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8237"
version_tuple = (0, 0, 8237)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8237")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8125"
data_version_tuple = (0, 0, 8125)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8125")
except ImportError:
    pass
data_git_hash = "b7b55724be513e0a91b22262d39bce279b98f8b0"
data_git_describe = "v0.0-8125-gb7b55724b"
data_git_msg = """\
commit b7b55724be513e0a91b22262d39bce279b98f8b0
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Tue Oct 12 11:44:58 2021 -0700

    [csrng/doc] fix app command flags table
    
    The markdown tags were in the wrong spot for row 3 of the flag0/clen table.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
