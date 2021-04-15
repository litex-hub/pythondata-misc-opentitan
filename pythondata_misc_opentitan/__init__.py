import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5872"
version_tuple = (0, 0, 5872)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5872")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5777"
data_version_tuple = (0, 0, 5777)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5777")
except ImportError:
    pass
data_git_hash = "0d63fe0a21729f9d8882c3aee387a05173d75a33"
data_git_describe = "v0.0-5777-g0d63fe0a2"
data_git_msg = """\
commit 0d63fe0a21729f9d8882c3aee387a05173d75a33
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Wed Mar 10 17:30:37 2021 -0800

    [ pwm, earlgrey ] Adding PWM to top_earlgrey
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
