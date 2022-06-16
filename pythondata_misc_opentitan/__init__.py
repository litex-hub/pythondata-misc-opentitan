import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12715"
version_tuple = (0, 0, 12715)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12715")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12573"
data_version_tuple = (0, 0, 12573)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12573")
except ImportError:
    pass
data_git_hash = "7004a27f1a7deab2bfd7419ce39eef2cb9c420f4"
data_git_describe = "v0.0-12573-g7004a27f1"
data_git_msg = """\
commit 7004a27f1a7deab2bfd7419ce39eef2cb9c420f4
Author: TIM EWINS <tim.ewins@ensilica.com>
Date:   Mon Jun 13 17:00:52 2022 +0100

    [flash_ctrl] Add Covergroup : error_cg
    
    Adds the covergroup error_cg which covers the fields of FLASH_CTRL.ERR_CODE
    
    Signed-off-by: TIM EWINS <tim.ewins@ensilica.com>

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
