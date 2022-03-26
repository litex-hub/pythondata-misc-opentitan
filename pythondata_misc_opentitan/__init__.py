import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11142"
version_tuple = (0, 0, 11142)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11142")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11016"
data_version_tuple = (0, 0, 11016)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11016")
except ImportError:
    pass
data_git_hash = "bf988e80dd06a7aec3f52d5cdeda41282bafbdae"
data_git_describe = "v0.0-11016-gbf988e80d"
data_git_msg = """\
commit bf988e80dd06a7aec3f52d5cdeda41282bafbdae
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Mar 25 13:18:35 2022 -0700

    [spi_host] Properly handle CPHA = 1
    
    This commit corrects the timing delays in the bit_shifting,
    byte_starting and byte_ending signals when operating in CPHA=1 mode.
    
    Also, since CPHA mode delays the shift register write pulses we
    have to delay the last_write pulse.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
