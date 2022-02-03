import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10049"
version_tuple = (0, 0, 10049)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10049")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9925"
data_version_tuple = (0, 0, 9925)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9925")
except ImportError:
    pass
data_git_hash = "611b1f855f6a631fc8a02844d9029c5e58f4daff"
data_git_describe = "v0.0-9925-g611b1f855"
data_git_msg = """\
commit 611b1f855f6a631fc8a02844d9029c5e58f4daff
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Feb 3 17:17:16 2022 +0100

    [aes/dv] Fix NIST vector test
    
    There were three issues causing this test to fail:
    1. The test was not correctly configuring the DUT for decryption. This
       has been introduced recently when modifying the main control
       register.
    2. The test did not wait for the DUT to be idle before writing the IV.
       This has been introduced recently when adding the key-touch-force-
       reseed feature.
    3. The IV got not correctly configured. Only the first word was written
       but to all 4 IV registers.
    
    All three issues are solved with this commit.
    
    This fixes lowRISC/OpenTitan#10544.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
