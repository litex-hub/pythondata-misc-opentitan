import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12731"
version_tuple = (0, 0, 12731)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12731")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12589"
data_version_tuple = (0, 0, 12589)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12589")
except ImportError:
    pass
data_git_hash = "093a576c313bed2249efcd82322c447c8eb7252d"
data_git_describe = "v0.0-12589-g093a576c3"
data_git_msg = """\
commit 093a576c313bed2249efcd82322c447c8eb7252d
Author: Dharanendra Kumar <dharanendra.kumar@ensilica.com>
Date:   Fri Jun 10 13:16:13 2022 +0100

    [PWM/DV] Updated Scoreboard And Added Stress Test
    
    - Modified The Scoreboard To Check Transction-By-Transaction
    - Modified The Base Test To Accomodate Counter Overflow
    
    Signed-off-by: dharanendrak <dharanendra.kumar@ensilica.com>
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
