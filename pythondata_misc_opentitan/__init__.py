import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13252"
version_tuple = (0, 0, 13252)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13252")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13110"
data_version_tuple = (0, 0, 13110)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13110")
except ImportError:
    pass
data_git_hash = "a91d59fa7fc7d87a0a2b2eb0cb033ccda80e5290"
data_git_describe = "v0.0-13110-ga91d59fa7f"
data_git_msg = """\
commit a91d59fa7fc7d87a0a2b2eb0cb033ccda80e5290
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Jul 15 15:03:46 2022 -0700

    [flash_ctrl] fixes for hanging transactions
    
    - propagate data error through the read pipeline and store
      it into the buffer if a buffer had been allocated.
    
    - any future reads that match this location will also error
      until evicted.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
