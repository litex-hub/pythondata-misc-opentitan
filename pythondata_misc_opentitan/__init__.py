import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14765"
version_tuple = (0, 0, 14765)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14765")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14623"
data_version_tuple = (0, 0, 14623)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14623")
except ImportError:
    pass
data_git_hash = "84ab1058db3805798f43ea3e42402940ec618b6b"
data_git_describe = "v0.0-14623-g84ab1058db"
data_git_msg = """\
commit 84ab1058db3805798f43ea3e42402940ec618b6b
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Oct 7 11:52:09 2022 -0700

    [chip dv] Fixes in chip_if and GPIO tests
    
    THis commit makes the following fixes to chip_if:
    - Fix the GPIO pin assignments (allocate the full set of
      32 chip IOs for the GPIO function)
    - Remove the default pulldowns on muxed IOs - these are not
      required.
    - Add default pulldown for the TAP strap and DFT IOs for certain
      LC states / pwrmgr phase. For the bulk of the tests, we use the
      RMA LC image which enables HW debug and DFT. This ends up allocating
      some of he muxed IOs for strap sampling. We may not intentionally
      exercise the TAP strap pins for most of these tests, so we need
      these pulldowns to prevent the strap sampling logic to interpret
      undriven IOs as Xs.
    - The removal of pulldowns on muxed IOs impacts UART tests. The
      UART smoke vseq is thus updated accordingly.
    - Finally, the GPIO test sequences are fixed to test the full
      set of 32 GPIOs.
    - Make ALL pins_if instances declared with PullStrength = Weak
      parameter.
    
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
