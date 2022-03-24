import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11083"
version_tuple = (0, 0, 11083)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11083")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10957"
data_version_tuple = (0, 0, 10957)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10957")
except ImportError:
    pass
data_git_hash = "a33ed81f41c3a31df0e8478e3c00303ad5616bbe"
data_git_describe = "v0.0-10957-ga33ed81f4"
data_git_msg = """\
commit a33ed81f41c3a31df0e8478e3c00303ad5616bbe
Author: Daniel Beitel <dbeitel@rivosinc.com>
Date:   Thu Jan 27 14:12:15 2022 -0800

    [sw,mask_rom] Configure Debug ROM in ePMP so debug can be enabled in RMA
    
    Fixes #10131
    
    Signed-off-by: Daniel Beitel <dbeitel@rivosinc.com>

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
