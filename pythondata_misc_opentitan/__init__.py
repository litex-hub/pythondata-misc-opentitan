import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11221"
version_tuple = (0, 0, 11221)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11221")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11095"
data_version_tuple = (0, 0, 11095)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11095")
except ImportError:
    pass
data_git_hash = "339e498ed31a10b9acc2bc2063a2cfdeb131948f"
data_git_describe = "v0.0-11095-g339e498ed"
data_git_msg = """\
commit 339e498ed31a10b9acc2bc2063a2cfdeb131948f
Author: Jason Hoddinett <jason.hoddinett.ensilica@opentitan.org>
Date:   Tue Mar 22 09:51:26 2022 +0000

    [pwm/dv] Added pwm_rand_output_vseq and environment changes
    
    Fixed any outstanding typos or mistakes
    
    Signed-off-by: Jason Hoddinett <jason.hoddinett.ensilica@opentitan.org>

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
