import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12978"
version_tuple = (0, 0, 12978)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12978")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12836"
data_version_tuple = (0, 0, 12836)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12836")
except ImportError:
    pass
data_git_hash = "a4684e1331fa7f64d091e37a1a4bda140cd3d4d1"
data_git_describe = "v0.0-12836-ga4684e1331"
data_git_msg = """\
commit a4684e1331fa7f64d091e37a1a4bda140cd3d4d1
Author: Dharanendra Kumar <dharanendra.kumar@ensilica.com>
Date:   Mon Jun 27 13:54:08 2022 +0100

    [PWM/DV] Updates For DV document
    
       Updated PWM DV document for V2
       PWM is ready for V2
       Updated review comments from Jadeon and Matute
    
    Signed-off-by: Dharanendra Kumar <dharanendra.kumar@ensilica.com>

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
