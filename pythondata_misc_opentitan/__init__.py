import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13255"
version_tuple = (0, 0, 13255)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13255")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13113"
data_version_tuple = (0, 0, 13113)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13113")
except ImportError:
    pass
data_git_hash = "106487eba9126c1d7cd0227502c625df29b55813"
data_git_describe = "v0.0-13113-g106487eba9"
data_git_msg = """\
commit 106487eba9126c1d7cd0227502c625df29b55813
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jul 22 16:09:06 2022 -0700

    [dv/chip] remove forced lc_dft_en value
    
    This PR removes the tb.sv file that force lc_dft_en to On.
    This is not needed because the loaded image is "rma" which enables the
    lc_dft_en signal. And the test waits until otp_init is done, so we won't
    drive any tlul transactions when `lc_dft_en` is Off.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
