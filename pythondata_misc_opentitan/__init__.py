import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14768"
version_tuple = (0, 0, 14768)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14768")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14626"
data_version_tuple = (0, 0, 14626)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14626")
except ImportError:
    pass
data_git_hash = "84fdd3bf374f168367ba7ffcb07cfa4d79c54875"
data_git_describe = "v0.0-14626-g84fdd3bf37"
data_git_msg = """\
commit 84fdd3bf374f168367ba7ffcb07cfa4d79c54875
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Oct 14 10:08:40 2022 -0700

    [entropy_src/rtl] Clear window_cntr on disable
    
    This commit reverts the window_cntr_clr behavior to the original design
    where this counter is cleared on disable.   When health_test_clr was
    changed to a pulse emitted on enable, this counter was left uncleared
    after disable.
    
    This has been observed to cause spurious `window_wrap_pulse`'s when
    reconfiguring the module, particularly if the window_size is shrunk
    while reconfiguring the DUT.
    
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
