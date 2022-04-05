import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11390"
version_tuple = (0, 0, 11390)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11390")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11264"
data_version_tuple = (0, 0, 11264)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11264")
except ImportError:
    pass
data_git_hash = "f8256d0b953b28646716cc17d091b9304b76dcc7"
data_git_describe = "v0.0-11264-gf8256d0b9"
data_git_msg = """\
commit f8256d0b953b28646716cc17d091b9304b76dcc7
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Thu Mar 31 07:09:11 2022 -0700

    [entropy_src/rtl] Prevent interrupt status for data valid
    
    For the mode where the entropy read register is not being used,
    the related FIFO state and interrupt status bits should be unchanging.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
