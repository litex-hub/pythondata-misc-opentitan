import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14881"
version_tuple = (0, 0, 14881)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14881")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14739"
data_version_tuple = (0, 0, 14739)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14739")
except ImportError:
    pass
data_git_hash = "f54491d31c43f8a181a941da78bd6fb89aa15311"
data_git_describe = "v0.0-14739-gf54491d31c"
data_git_msg = """\
commit f54491d31c43f8a181a941da78bd6fb89aa15311
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Wed Oct 12 07:35:38 2022 +0000

    [top/dv] Fix filename of Ibex lockstep glitch vseq
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
