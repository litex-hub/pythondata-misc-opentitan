import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10203"
version_tuple = (0, 0, 10203)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10203")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10079"
data_version_tuple = (0, 0, 10079)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10079")
except ImportError:
    pass
data_git_hash = "411856a57b97156ea8f5fa9a5f7e2a3993ebe67b"
data_git_describe = "v0.0-10079-g411856a57"
data_git_msg = """\
commit 411856a57b97156ea8f5fa9a5f7e2a3993ebe67b
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Tue Feb 8 12:25:12 2022 -0800

    [spi_host] Fix bug around invalid direction detection.
    
    Dual and Qual mode transactions are invalid if the are bidirectional.
    Previously this code flagged an error if such segments were anything
    but bidirectional.
    
    Bug first noted in #10680.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
