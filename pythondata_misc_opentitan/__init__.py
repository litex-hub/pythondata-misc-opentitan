import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8754"
version_tuple = (0, 0, 8754)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8754")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8642"
data_version_tuple = (0, 0, 8642)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8642")
except ImportError:
    pass
data_git_hash = "496276004c4215299ac4d03af5516344ce3c5b25"
data_git_describe = "v0.0-8642-g496276004"
data_git_msg = """\
commit 496276004c4215299ac4d03af5516344ce3c5b25
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Nov 15 16:58:28 2021 +0000

    [dv] Fix shape calculations for replicated ECC
    
    data_width is supposed to be the width of a word in bits, not counting
    any ECC bits. The computation that was there before wasn't quite
    right because it didn't allow for the possibility of multiple
    subwords. We use this structure for OTBN, where we have 256-bit words,
    split into eight 32-bit subwords where each is protected with the
    Ecc_39_32 scheme.
    
    Also bump up the maximum bytes per word (we need more!) and add
    read256() and write256() functions.
    
    Finally, fix the instantiations of imem_util and dmem_util in the OTBN
    testbench (I'd misunderstood what the n_bits argument did).
    
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
