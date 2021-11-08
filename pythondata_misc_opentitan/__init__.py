import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8623"
version_tuple = (0, 0, 8623)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8623")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8511"
data_version_tuple = (0, 0, 8511)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8511")
except ImportError:
    pass
data_git_hash = "40f72477995d57ef4e53b1568271e6414fd9d786"
data_git_describe = "v0.0-8511-g40f724779"
data_git_msg = """\
commit 40f72477995d57ef4e53b1568271e6414fd9d786
Author: Udi Jonnalagadda <udij@google.com>
Date:   Tue Jun 22 15:19:20 2021 -0700

    [dv/sram] Enable multi-ral
    
    This PR enables full multi-ral functionality in the SRAM testbench, and
    to that end does a couple of related things:
    
    - Adds a custom reg model for the memory primitive, this is needed since
      different parameterizations of the TB will be reused at the
      chip-level.
    - General updates to the scoreboard and rest of the environment to make
      use of the built-in TL arrays in the base env_cfg classes, and remove
      the explicitly defined tl_agent initially used for the memory
      interface.
    - Remove the `mem_tl_errors` test as we can now rely on the automated
      test suite.
    - Parameterize the entire SRAM testbench accordingly to allow reuse at
      the chip-level.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
