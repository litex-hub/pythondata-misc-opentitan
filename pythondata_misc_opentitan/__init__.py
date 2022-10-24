import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14911"
version_tuple = (0, 0, 14911)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14911")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14769"
data_version_tuple = (0, 0, 14769)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14769")
except ImportError:
    pass
data_git_hash = "ffab90e6a8123980561696ac528fc162f9801893"
data_git_describe = "v0.0-14769-gffab90e6a8"
data_git_msg = """\
commit ffab90e6a8123980561696ac528fc162f9801893
Author: Jade Philipoom <jadep@google.com>
Date:   Mon Oct 24 17:26:00 2022 +0200

    [rom] Fix pinmux indexing and set attributes first.
    
    The pinmux initialization previously used the pinmux input selector
    value as the pad index, which results in an off-by-two error since the
    input selector is (pad index + 2).
    
    Also, the pinmux documentation specifies that pad attributes should be
    set first, before configuring the pinmux matrix, so this change moves
    attribute-setting to precede IO configuration.
    
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
