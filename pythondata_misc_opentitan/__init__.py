import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15157"
version_tuple = (0, 0, 15157)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15157")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15015"
data_version_tuple = (0, 0, 15015)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15015")
except ImportError:
    pass
data_git_hash = "f3da3f66ef03e2485f51e7626d5dc46a93273ac5"
data_git_describe = "v0.0-15015-gf3da3f66ef"
data_git_msg = """\
commit f3da3f66ef03e2485f51e7626d5dc46a93273ac5
Author: Michael Schaffner <msf@google.com>
Date:   Wed Nov 2 13:13:41 2022 -0700

    [dv] Always preload ROM in chip_base_vseq
    
    chip_stub_cpu_base_vseq which caused the ROM init done check in
    dut_init() of the chip_rv_dm_lc_disabled_vseq to hang forever.
    
    This PR removes the ROM init check from chip_rv_dm_lc_disabled_vseq
    to fix that. In addition, it always pre-loads a valid ROM image
    during the pre_start() phase of chip_base_vseq to make sure that
    the ROM check can succeed successfully. Note that the real hardware
    will always contain a valid ROM image, so this is not a simulation-only
    hack and bring simulations closer to the behavior of the real hardware.
    
    This fixes #15893.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
