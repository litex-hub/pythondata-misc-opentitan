import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15315"
version_tuple = (0, 0, 15315)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15315")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15173"
data_version_tuple = (0, 0, 15173)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15173")
except ImportError:
    pass
data_git_hash = "2a6284b002fb48193ac9cfee06b679cdd76538d5"
data_git_describe = "v0.0-15173-g2a6284b002"
data_git_msg = """\
commit 2a6284b002fb48193ac9cfee06b679cdd76538d5
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Nov 4 15:54:46 2022 -0700

    [chip dv] Fix chip_sw_rom_ctrl_integrity_check test
    
    - Check rom_ctrl is reporting bad intg with an internal probe
    - Pick a digest addr randomly to indroduce corruption, rather the only the
      last digest word.
    - Corrupt the digest with only a single bit-flip in the digest word, including
      the integrity bits, rather than corrupting the whole word.
    - In the second phase of the test, wait for the ROM operation to be completed first
      (this is the main issue described in #16013).
    
    Fixed #16013.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
