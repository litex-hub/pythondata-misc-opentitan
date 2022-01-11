import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9424"
version_tuple = (0, 0, 9424)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9424")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9306"
data_version_tuple = (0, 0, 9306)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9306")
except ImportError:
    pass
data_git_hash = "eadef042fa31019ab3174d6c48ab743b9af40495"
data_git_describe = "v0.0-9306-geadef042f"
data_git_msg = """\
commit eadef042fa31019ab3174d6c48ab743b9af40495
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Mon Jan 10 07:54:25 2022 +0000

    [rom_ctrl, dv] combined successful_rom_chk test with smoke test
    
    Based on V1 review comments, successful_rom_chk test is combined with
    rom_ctrl_smoke testcase.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
