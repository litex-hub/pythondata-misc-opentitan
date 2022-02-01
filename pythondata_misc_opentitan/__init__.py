import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9928"
version_tuple = (0, 0, 9928)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9928")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9804"
data_version_tuple = (0, 0, 9804)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9804")
except ImportError:
    pass
data_git_hash = "20c314947936d044071f2820570c22d9f3ba913f"
data_git_describe = "v0.0-9804-g20c314947"
data_git_msg = """\
commit 20c314947936d044071f2820570c22d9f3ba913f
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Jan 31 12:17:57 2022 -0800

    [dv, mem_bkdr_util] Fix ECC-computed backdoor WRs
    
    - Minor enhancement to 'global' mem modification methods
      (set|clear|randomize|invalidate_mem()) - manipulate the entire array
      rather than go byte-by-byte, which is computationally much slower
    - It also fixes the flash case which has the unaddressable metadata bits
      (first level ECC) at [67:64].
    - Refactor the ECC computation into its own function for reuse and
      extension.
    - Extend the class for flash customization - for flash, override the
      `get_ecc_computed_data()` to perform 2 level ECC. Likewise, override
      the randomize_mem() to similar effect.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
