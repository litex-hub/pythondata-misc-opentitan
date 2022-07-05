import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12937"
version_tuple = (0, 0, 12937)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12937")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12795"
data_version_tuple = (0, 0, 12795)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12795")
except ImportError:
    pass
data_git_hash = "6a643647dde9851c1b612d7219e783a03713946f"
data_git_describe = "v0.0-12795-g6a643647dd"
data_git_msg = """\
commit 6a643647dde9851c1b612d7219e783a03713946f
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Jul 1 14:25:30 2022 -0700

    [pwm/doc] Explicitly document pwm_en_o outputs
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
