import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11284"
version_tuple = (0, 0, 11284)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11284")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11158"
data_version_tuple = (0, 0, 11158)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11158")
except ImportError:
    pass
data_git_hash = "ad62950332301dbe0445f3ef7f023be595645d52"
data_git_describe = "v0.0-11158-gad6295033"
data_git_msg = """\
commit ad62950332301dbe0445f3ef7f023be595645d52
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Fri Apr 1 15:44:36 2022 +0100

    [adc_ctrl/dv] Updated ADC_CTRL DV documents
    
    - Updated ADC_CTRL DV documents
    
    Signed-off-by: Nigel Scales <nigel.scales@gmail.com>

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
