import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13329"
version_tuple = (0, 0, 13329)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13329")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13187"
data_version_tuple = (0, 0, 13187)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13187")
except ImportError:
    pass
data_git_hash = "18563abecc18c4802476d48df61d8c477eb42ad1"
data_git_describe = "v0.0-13187-g18563abecc"
data_git_msg = """\
commit 18563abecc18c4802476d48df61d8c477eb42ad1
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Feb 22 23:08:35 2022 +0000

    [otbn] Update bus accessible size to 3kiB
    
    After some discussion, this looks like the safest approach: the
    1kiB scratchpad should still be big enough to hold any key data but
    we've got a bit more headroom on the bus accessible part.
    
    To make the RSA routines work with the reduced scratchpad, we need to
    reduce the software buffers accordingly:
    - m0d occupies always 32 bytes.
    - RR occupies N*32 bytes where N is the number of 256 limbs per bignum
      which is 16 for RSA-4096. This means RR needs at most 512 bytes.
    - work_buf occupies the remaining 480 bytes of the scratchpad.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
