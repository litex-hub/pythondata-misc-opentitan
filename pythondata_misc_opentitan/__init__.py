import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8410"
version_tuple = (0, 0, 8410)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8410")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8298"
data_version_tuple = (0, 0, 8298)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8298")
except ImportError:
    pass
data_git_hash = "e780525312581e2a6813a26e36c272a114a12118"
data_git_describe = "v0.0-8298-ge78052531"
data_git_msg = """\
commit e780525312581e2a6813a26e36c272a114a12118
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Thu Oct 21 13:47:54 2021 +0100

    [mask_rom] Enable flash execution after signature verification
    
    Rather than enabling flash execution immediately wait until
    signature verfication is complete.
    
    Placed before the `sec_mmio` expectation checks so that the
    expectation checks are sandwiched between the flash execution enable
    and the ePMP region unlock.
    
    Updates #7834
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
