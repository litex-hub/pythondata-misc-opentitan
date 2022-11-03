import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15166"
version_tuple = (0, 0, 15166)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15166")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15024"
data_version_tuple = (0, 0, 15024)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15024")
except ImportError:
    pass
data_git_hash = "3e32a31a2ba47298a1041913daa27e827b5068b0"
data_git_describe = "v0.0-15024-g3e32a31a2b"
data_git_msg = """\
commit 3e32a31a2ba47298a1041913daa27e827b5068b0
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Nov 2 22:03:03 2022 -0700

    [chip dv] Fixes for failing CSR tests
    
    Fixes chip_csr_hw_reset test with failure signature:
    ```
      UVM_ERROR @ 2823.589889 us: (chip_if.sv:146) [tb.dut.chip_if] Detected an X on MioPadIor13
    ```
    - Added weak pulls on DIOs for this test, since it randomly writes pinmux pad attr
      and wake up registers and inadvertently creates a combination that ends up spewing Xs.
    
    Fixes chip_csr_bit_bash test with failure signature:
    ```
    Job chip_earlgrey_asic-sim-vcs_run_cover_reg_top killed due to: Exit reason: User job exceeded
    runlimit: User job timed out has 1 failures:
    ```
    - Limited the number of CSRs tested for bit bash to 200 at a time, increased
      test timeout to 180 minutes.
    
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
