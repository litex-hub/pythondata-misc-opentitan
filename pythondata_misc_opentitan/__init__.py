import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15022"
version_tuple = (0, 0, 15022)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15022")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14880"
data_version_tuple = (0, 0, 14880)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14880")
except ImportError:
    pass
data_git_hash = "ae4960e1159a09a16611ce5883da8217d84c405a"
data_git_describe = "v0.0-14880-gae4960e115"
data_git_msg = """\
commit ae4960e1159a09a16611ce5883da8217d84c405a
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Tue Oct 25 21:26:24 2022 -0700

    [entropy_src/dv] Fine tune extht timing cases (DV)
    
    This commit fixes DV corner cases to capture the last RNG data accepted
    into the DUT before it is disabled.  Since the new EXTHT agent
    introduces a slight synchronization delay this adjustment is needed to
    make sure that all samples are counted.
    
    In the worst case the window_wrap_pulse ends two cycles after the DUT
    has been disabled. (One cycle if RNG bit selection is disabled two
    if it is enabled) Rather than dumping the a partial HT window
    immediately when the DUT is disabled, wait these extra two cycles to
    catch the last sample.
    
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
