import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12888"
version_tuple = (0, 0, 12888)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12888")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12746"
data_version_tuple = (0, 0, 12746)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12746")
except ImportError:
    pass
data_git_hash = "c18d47641210a2d060550bb2cbf447c98e3d8b61"
data_git_describe = "v0.0-12746-gc18d476412"
data_git_msg = """\
commit c18d47641210a2d060550bb2cbf447c98e3d8b61
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Jun 25 16:30:37 2022 -0700

    [entropy_src/dv] bit_sel_en timing adjustment
    
    In bit_sel_en the DUT has a timing idiosyncracy in which
    the selected RNGs bits remain in the bit select pfifo until
    one more RNG sample is acquired.  This does not violate the
    spec in any way, but can lead to test failures if the
    scoreboard is expecting the last sample to be included in
    the health checks.
    
    This commit adjusts the scoreboarding to mimic this feature
    and properly predict which samples are included in the health
    test statistics in bit select mode.
    
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
