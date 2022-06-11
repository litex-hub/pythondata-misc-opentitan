import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12642"
version_tuple = (0, 0, 12642)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12642")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12500"
data_version_tuple = (0, 0, 12500)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12500")
except ImportError:
    pass
data_git_hash = "748d19a672cd3181a2fa57caf5ebf56df207f508"
data_git_describe = "v0.0-12500-g748d19a67"
data_git_msg = """\
commit 748d19a672cd3181a2fa57caf5ebf56df207f508
Author: Drew Macrae <drewmacrae@google.com>
Date:   Mon Jun 6 13:51:47 2022 -0400

    [ci] re-add mask_rom_epmp_test_sim_verilato r
    
    Co-authored-by: Timothy Trippel <5633066+timothytrippel@users.noreply.github.com>
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
