import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13141"
version_tuple = (0, 0, 13141)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13141")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12999"
data_version_tuple = (0, 0, 12999)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12999")
except ImportError:
    pass
data_git_hash = "4a7932628d9bca84c7d631528df7175886e2f551"
data_git_describe = "v0.0-12999-g4a7932628d"
data_git_msg = """\
commit 4a7932628d9bca84c7d631528df7175886e2f551
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sun Jul 10 13:38:16 2022 -0700

    [entropy_src] Implement Error and Alert related covergroups
    
    This PR updates the test plan to expands the err_test_cg in to several
    smaller covergroups that are easier to sample.
    
    Since the original err_test_cg covers so many disparate classes of
    events that happen at different times, it would be hard to write a
    single sample function that covers them all.   Therefore this CG has
    been broken into 5 smaller coverpoints:
    
     - `err_test_cg`: covers that writes to ERR_CODE_TEST generate the
        expected alerts for all bits
     - `mubi_err_cg`: covers that we've tested that writes to registers that
        expect redundancy in their values (including both MultiBit Booleans
        and the AlertThreshold numeric register), and that alerts are seen
        when bad values are inserted.
     - `sm_err_cg` covers that we've seen alerts when that the MAIN_SM and
        ACK_SM are forced into invalid values
     - `fifo_err_cg` covers that we've seen alerts when the FIFOs
        malfunction.
     - `cntr_err_cg` covers that all redundant counters have been forced to
        mismatching values.
    
    NOTE: Alerts related to health tests (i.e. the main_sm _recoverable_
          alert) are covered by other HT related coverpoints.
    
    In terms of implementation Sampling and scoreboarding has been updated
    to support sampling of the new err_test_cg.  entropy_src_rng_vseq
    has also been updated to generate ERR_CODE_TEST events.
    
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
