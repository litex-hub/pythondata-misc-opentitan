import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5551"
version_tuple = (0, 0, 5551)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5551")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5456"
data_version_tuple = (0, 0, 5456)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5456")
except ImportError:
    pass
data_git_hash = "edbd19b2f9d21161d5a4aa781fc89a2bfd515855"
data_git_describe = "v0.0-5456-gedbd19b2f"
data_git_msg = """\
commit edbd19b2f9d21161d5a4aa781fc89a2bfd515855
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Tue Feb 23 21:53:18 2021 +0000

    [sw, dif_sram_ctrl] Add DIF header and checklist for SRAM Controller
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
