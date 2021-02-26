import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5159"
version_tuple = (0, 0, 5159)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5159")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5068"
data_version_tuple = (0, 0, 5068)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5068")
except ImportError:
    pass
data_git_hash = "d812401e0220ecc4f6471b9b3d54175ded8d0dd3"
data_git_describe = "v0.0-5068-gd812401e0"
data_git_msg = """\
commit d812401e0220ecc4f6471b9b3d54175ded8d0dd3
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Wed Jan 20 16:37:27 2021 +0000

    [sw, pmp] Add new enhanced PMP C API
    
    Add an API to create, configure and commit entries to the PMP
    control registers. Updates are performed using 'transactions'.
    Transactions must be initialized before use with the number of
    regions that are to be configured. This will then be checked
    when the transaction is finalized and the CSRs are updated.
    
    Unlike the existing PMP API we specify all region types the same
    way using a struct containing `start` and `end` addresses. This
    makes it easy to be explicit about the region boundaries as shown
    in the example below.
    
    The new EPMP API assumes that most `mseccfg` updates will occur in
    assembly and that the API will only be used to disable the Rule
    Locking Bypass (`msecffg.RLB`) feature. In particular this API
    assumes that Machine Mode Lockdown (`mseccfg.MML`) will be
    disabled (though that can be verified by a call to `epmp_check`.)
    
    The API has been designed so that Machine Mode Lockdown support
    can be added at a later date if required by adding an additional
    set of `Lockdown` permission enum values. It would make the API
    clunkier though.
    
    Example (configure and set in a single transaction):
    
      ```
      // Initialize the library with the current state of the PMP
      // CSRs.
      res0 = epmp_init();
    
      // Enable Rule Locking Bypass (RLB).
      res1  = epmp_set_rule_locking_bypass(kEpmpRlbToggleEnabled);
    
      // Update 4 PMP entries in a single transaction.
      res2 = epmp_transaction_start(kEpmpEntryCount4);
      res3 = epmp_entry_configure_na4(kEpmpEntry0,
                 (epmp_region_t){ .start = 0x0, .end = 0x4 },
                 kEpmpPermLockedReadWrite);
      res4 = epmp_entry_configure_napot(kEpmpEntry1,
                 (epmp_region_t){ .start = 0x40, .end = 0x48 },
                 kEpmpPermLockedReadExecute);
      // pmpaddr2 used as base address for entry 3
      res5 = epmp_entry_configure_tor(kEpmpEntry3,
                 (epmp_region_t){ .start = 0x100, .end = 0x200 },
                 kEpmpPermLockedReadWrite);
      res6 = epmp_entry_configure_tor(kEpmpEntry4,
                 (epmp_region_t){ .start = 0x200, .end = 0x300 },
                 kEpmpPermLockedReadOnly);
      res7 = epmp_transaction_end(kEpmpEntryCount4); // update CSRs
    
      ```
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
