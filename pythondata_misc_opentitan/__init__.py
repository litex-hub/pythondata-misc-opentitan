import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8580"
version_tuple = (0, 0, 8580)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8580")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8468"
data_version_tuple = (0, 0, 8468)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8468")
except ImportError:
    pass
data_git_hash = "755ea76e80583f4bb41aa0b02ad2a40a60eaa48f"
data_git_describe = "v0.0-8468-g755ea76e8"
data_git_msg = """\
commit 755ea76e80583f4bb41aa0b02ad2a40a60eaa48f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Oct 22 15:21:23 2021 +0100

    [dv] Massively shorten FOO_csr_mem_rw_with_rand_reset tests
    
    These tests are intended to mess around with memory and then suddenly
    pull the reset line at unexpected times. Since the device is quiescent
    otherwise, the "time constant" for the sort of state we're trying to
    hit edge cases in is only a few TL transactions' worth. Since a TL
    transaction only takes ~10 cycles, there's no real need to delay
    millions of cycles before injecting the reset.
    
    However, we don't also want to shorten the delay to reset for the
    stress_all_with_rand_reset tests, because that would mean we hardly
    did any transactions between each reset.
    
    So we leave the existing constraint unchanged (except slightly
    changing the name to make it describe what's going on better), but
    allow a caller of run_stress_all_with_rand_reset_vseq() to pass an
    argument called reset_delay_bound. This defaults to a massive number
    so will have no effect unless provided.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
