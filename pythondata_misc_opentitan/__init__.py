import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14475"
version_tuple = (0, 0, 14475)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14475")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14333"
data_version_tuple = (0, 0, 14333)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14333")
except ImportError:
    pass
data_git_hash = "00cd9905a54c30132213247161570efae2d24447"
data_git_describe = "v0.0-14333-g00cd9905a5"
data_git_msg = """\
commit 00cd9905a54c30132213247161570efae2d24447
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Sep 27 22:56:34 2022 -0700

    [dv,rom_e2e] update testplan to only track P1 tests in nightlies
    
    This updates the ROM E2E testplan and chip_sim_cfg.hjson file on only
    track P1 ROM E2E tests in the DV nightly regression to reflect current
    efforts.
    
    This fixes #15009.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
