import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11224"
version_tuple = (0, 0, 11224)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11224")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11098"
data_version_tuple = (0, 0, 11098)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11098")
except ImportError:
    pass
data_git_hash = "7626f30897de5f85dd530e01da50f01b6e04a503"
data_git_describe = "v0.0-11098-g7626f3089"
data_git_msg = """\
commit 7626f30897de5f85dd530e01da50f01b6e04a503
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 24 13:58:07 2022 -0700

    [flash_ctrl] d2s review fixes
    
    - convert lc compare to lc_tx_test_true_strict
    - expand disable usage to more fsms
    - add additional prim counters to lcmgr
    - Add countermeasure clarifications
    - switch to mubi sync where appropriate
    - Add tlul_lc_gate in front of adapter sram to error back
      transactions when disabled
    - documentation updates and clarifications
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
