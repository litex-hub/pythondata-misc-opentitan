import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11466"
version_tuple = (0, 0, 11466)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11466")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11340"
data_version_tuple = (0, 0, 11340)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11340")
except ImportError:
    pass
data_git_hash = "c19face3711d149f7befa6c8fdee08b90f8c172a"
data_git_describe = "v0.0-11340-gc19face37"
data_git_msg = """\
commit c19face3711d149f7befa6c8fdee08b90f8c172a
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Wed Apr 6 11:06:01 2022 -0400

    [mask_rom] Add a separate library for .static_critical symbols
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
