import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9284"
version_tuple = (0, 0, 9284)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9284")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9171"
data_version_tuple = (0, 0, 9171)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9171")
except ImportError:
    pass
data_git_hash = "5c710272c119a859e495b517e8833aea95eadd5f"
data_git_describe = "v0.0-9171-g5c710272c"
data_git_msg = """\
commit 5c710272c119a859e495b517e8833aea95eadd5f
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Dec 17 16:52:42 2021 -0800

    [ entropy_src, dv] Scoreboarding for Health Checks
    
    (Note: Some checks disabled in scoreboard due to bugs in DUT)
    
    - Health check scoreboarding is now functional
      - Monitors input RNG, and applies health checks independently
      - Creates predictions for watermarks, failures, and alerts
      - Applies thresholds based on live register settings
        - Handles both FIPS and BYPASS settings (still tesing BYPASS only, in smoke test)
      - Base vseq now checks all watermark values at end of sim.
      - Thresholds currently set to maximum tolerance, will test thresholds in a future PR
    - Some differences in IP discovered
      - Watermark registers are are not matching for the following tests: repcnt, repcnts
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post113"
tool_version_tuple = (0, 0, 113)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post113")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
