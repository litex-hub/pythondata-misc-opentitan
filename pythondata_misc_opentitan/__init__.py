import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12926"
version_tuple = (0, 0, 12926)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12926")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12784"
data_version_tuple = (0, 0, 12784)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12784")
except ImportError:
    pass
data_git_hash = "435d6c889ddf86d116086ea964e125616bfa0c51"
data_git_describe = "v0.0-12784-g435d6c889d"
data_git_msg = """\
commit 435d6c889ddf86d116086ea964e125616bfa0c51
Author: Dharanendra Kumar <dharanendra.kumar@ensilica.com>
Date:   Tue Jun 28 19:24:12 2022 +0100

    [PWM/DV] Corrections In PWM Scoreboard
    
       Made corrections in subcycle_cnt initialization
       Synchronized the PWM scoreboard and DUT pwm_o pulse
       Some more tweak to scoreboard
       Updated review comments related to localparam
    
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
