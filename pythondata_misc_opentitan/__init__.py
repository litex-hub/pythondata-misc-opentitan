import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5304"
version_tuple = (0, 0, 5304)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5304")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5209"
data_version_tuple = (0, 0, 5209)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5209")
except ImportError:
    pass
data_git_hash = "c43c58ba78f1d8fdbfccd8db240926eed6f13923"
data_git_describe = "v0.0-5209-gc43c58ba7"
data_git_msg = """\
commit c43c58ba78f1d8fdbfccd8db240926eed6f13923
Author: Tarik Graba <tarik.graba@telecom-paris.fr>
Date:   Mon Mar 8 13:58:30 2021 +0100

    [dv/dpi] Fix assignment to SystemVerilog chandle
    
    Section 6.14 of the standard states that assignment to chandle can only
    be made from `null` or an other chandle, not from an integer literal.
    
    This patch allows the compilation of the simulation models with modelsim
    
    Signed-off-by: Tarik Graba <tarik.graba@telecom-paris.fr>

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
