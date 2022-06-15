import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12696"
version_tuple = (0, 0, 12696)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12696")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12554"
data_version_tuple = (0, 0, 12554)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12554")
except ImportError:
    pass
data_git_hash = "4b99935e1fa19b3362a302ac830753e3b8b17650"
data_git_describe = "v0.0-12554-g4b99935e1"
data_git_msg = """\
commit 4b99935e1fa19b3362a302ac830753e3b8b17650
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Jun 14 10:18:55 2022 -0400

    [ci] Update CI and run-fgpa-cw310-tests.sh to use the bitstream with mask_rom
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
