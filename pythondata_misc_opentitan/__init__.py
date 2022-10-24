import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14902"
version_tuple = (0, 0, 14902)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14902")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14760"
data_version_tuple = (0, 0, 14760)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14760")
except ImportError:
    pass
data_git_hash = "94c65bf3f885873f08306647ed497d30fd66f55c"
data_git_describe = "v0.0-14760-g94c65bf3f8"
data_git_msg = """\
commit 94c65bf3f885873f08306647ed497d30fd66f55c
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Wed Oct 19 13:20:41 2022 -0700

    [entropy_src/doc] remove reference to rate
    
    The ES documentation refers to the word "rate", which is a reference to the
    former LFSR rate control register. Since this register and function have been
    removed for security reasons, the documentation needed an update to match.
    Fixes #13336.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
