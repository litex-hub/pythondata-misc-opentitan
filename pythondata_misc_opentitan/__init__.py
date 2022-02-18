import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10415"
version_tuple = (0, 0, 10415)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10415")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10289"
data_version_tuple = (0, 0, 10289)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10289")
except ImportError:
    pass
data_git_hash = "9e0c16ad01c788c14350770a7465c4886771a865"
data_git_describe = "v0.0-10289-g9e0c16ad0"
data_git_msg = """\
commit 9e0c16ad01c788c14350770a7465c4886771a865
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Thu Feb 17 17:16:31 2022 -0800

    [entropy_src/dv] Program thresholds before enabling
    
    The health test thresholds (which are configured by test-specific
    routines) must be programmed before the module_enable or sw_regupd
    registers.  This commit fixes the rng vseq to postpone the base vseq
    initialization (the bulk of the register configuration) until after
    the thresholds have been loaded.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
