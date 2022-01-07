import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9385"
version_tuple = (0, 0, 9385)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9385")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9268"
data_version_tuple = (0, 0, 9268)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9268")
except ImportError:
    pass
data_git_hash = "e05b0e5e0c99970cb7fb79124b44dbf5fa15455b"
data_git_describe = "v0.0-9268-ge05b0e5e0"
data_git_msg = """\
commit e05b0e5e0c99970cb7fb79124b44dbf5fa15455b
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Jan 7 05:57:03 2022 -0800

    [csrng/doc] fix lc_hw_debug_en comment
    
    The statement in the hjson file is not true anymore, removed.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
