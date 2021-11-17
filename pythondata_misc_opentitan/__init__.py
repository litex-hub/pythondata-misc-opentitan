import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8744"
version_tuple = (0, 0, 8744)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8744")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8632"
data_version_tuple = (0, 0, 8632)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8632")
except ImportError:
    pass
data_git_hash = "e10dfaf312614ae9ebcdfb8c79840de4cf45be7e"
data_git_describe = "v0.0-8632-ge10dfaf31"
data_git_msg = """\
commit e10dfaf312614ae9ebcdfb8c79840de4cf45be7e
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Nov 9 17:28:56 2021 +0000

    [otbn,dv] Teach otbn_model to pass validity bits to and from the ISS
    
    The binary file format has changed and now consists of 5 bytes for
    each 32-bit word. The first byte is a "validity byte", which should
    have value 0 (for invalid) or 1 (for valid). The other 4 bytes are a
    little-endian encoded 32-bit word.
    
    The first change in otbn_model is to use Ecc32MemArea's new
    ReadWithIntegrity method to get the integrity bits as well as the raw
    data. We then pass this to the ISS in the new format. In the other
    direction (reading data from the ISS), we have to parse the new format
    and also need to tweak our correctness check.
    
    Note that there's a temporary hack (with TODO message) here, which
    will go away once we've implemented integrity bits properly on the ISS
    side.
    
    On the ISS side, the only work is to read and write the new file
    format (with struct format string "<BI") and fix up the various bits
    of packing logic. There's a corresponding hack (also with TODO
    message), reminding us to handle validity bits properly when loading
    DMEM.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
