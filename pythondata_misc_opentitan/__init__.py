import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12780"
version_tuple = (0, 0, 12780)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12780")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12638"
data_version_tuple = (0, 0, 12638)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12638")
except ImportError:
    pass
data_git_hash = "87062e69f17ddc7a4f641796e2cc09d36e13176c"
data_git_describe = "v0.0-12638-g87062e69f1"
data_git_msg = """\
commit 87062e69f17ddc7a4f641796e2cc09d36e13176c
Author: Dharanendra Kumar <dharanendra.kumar@ensilica.com>
Date:   Tue Jun 21 14:30:34 2022 +0100

    [PWM/DV] Updated Checker For issue #13200
    
      Updated pwm_scoreboard.sv to accomodate the changes in RTL
      For the issue #13200
    
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
