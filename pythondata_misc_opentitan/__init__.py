import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15020"
version_tuple = (0, 0, 15020)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15020")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14878"
data_version_tuple = (0, 0, 14878)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14878")
except ImportError:
    pass
data_git_hash = "839eec77e69327a6708f9163bd78965a008a879c"
data_git_describe = "v0.0-14878-g839eec77e6"
data_git_msg = """\
commit 839eec77e69327a6708f9163bd78965a008a879c
Author: Michael Schaffner <msf@google.com>
Date:   Thu Oct 27 21:05:21 2022 -0700

    Update lowrisc_ibex to lowRISC/ibex@5f5a70fc
    
    Update code from upstream repository
    https://github.com/lowRISC/ibex.git to revision
    5f5a70fca90917cc6152be4b1e4d9679d0357a3b
    
    * Tweak regressions around PMP, allow for double_faults,
      uninit_accesses (Marno van der Maas)
    * [dv] Disable bad integrity on uninitialised memory for selected
      tests (Greg Chadwick)
    * [dv] Add single step over exception coverpoint (Greg Chadwick)
    * [dv] Remove `cp_insn_trigger_exception` coverpoint (Greg Chadwick)
    * [rtl] Fix ebreak debug cause (Greg Chadwick)
    * Fix bug in passing cosim_agent handle to the data_intf_seq (Harry
      Callahan)
    * Update google_riscv-dv to google/riscv-dv@ada58fc (Harry Callahan)
    * [rtl] Protect core_busy_o with a multi-bit encoding (Pirmin Vogel)
    * [dv] Add cpuctrlsts writes to riscv_rand_instr_test (Greg Chadwick)
    * [dv] Fix RVFI stage valid logic (Greg Chadwick)
    * [cosim] Implement double fault detection (Greg Chadwick)
    * Add wall-clock timeout within rtl simulation to gracefully end
      (Harry Callahan)
    * Add mechanism for test-specific timeout (Harry Callahan)
    * Fixup mem_intf seq to update cosim mem on DMEM uninit accesses
      (Harry Callahan)
    * Change ibex_mem_intf_response_seq to handle uninit memory
      differently (Harry Callahan)
    * [lint] Shellcheck bash scripts in repo (Marno van der Maas)
    * [rtl] Assert that dummy instructions only write R0 (Andreas Kurth)
    * [fcov,pmp] Illegal PMP write coverpoints check dside request error
      not low (Marno van der Maas)
    * Update google_riscv-dv to google/riscv-dv@e0eae9e (Canberk Topal)
    * [vcs] Fix Ibex DV runs for VCS (Canberk Topal)
    * Change double_fault detector to on by default, fatal error if
      triggered (Harry Callahan)
    * Add a double_fault detector to core_ibex uvm environment (Harry
      Callahan)
    * [dv] Use fetch enable sequence by default (Greg Chadwick)
    * [dv] Increase various timeouts (Greg Chadwick)
    * [dv] fetch_enable_seq tweaks (Greg Chadwick)
    * [rtl] Immediately stop execution when fetch disabled (Greg Chadwick)
    * Fixup signal used when checking for ebreak cause (Harry Callahan)
    * [rtl] Change how we record debug causes (Canberk Topal)
    * [rtl/dv] Bring back data integrity check on write responses (Greg
      Chadwick)
    * [dv] Remove riscv_perf_counter_test (Greg Chadwick)
    * [dv] Remove CPUCTRLSTS from riscv_csr_test (Greg Chadwick)
    * [rtl] Ignore MIE bit in U mode (Greg Chadwick)
    * [rtl] Don't take interrupts when single stepping (Greg Chadwick)
    * Update google_riscv-dv to google/riscv-dv@c6acc18 (Harry Callahan)
    * [dv] Shellcheck prettify script (Marno van der Maas)
    * [dv] Shellcheck objdump script and check for RISCV_TOOLCHAIN
      variable (Marno van der Maas)
    * [dv] Add MHPM Counter number param to SpikeCosim (Canberk Topal)
    * [doc] Add NAPOT address mode to coverage plan (Marno van der Maas)
    * [pmp] Add coverpoints for large NAPOT regions (Marno van der Maas)
    * single_step test : only drive debug_req_i after stepping finishes
      (Harry Callahan)
    * Single step debugging test changes for fcov (Harry Callahan)
    * [if,pmp] Check second bit instead of third for instruction alignment
      (Marno van der Maas)
    * Change failure modes and add comments with more clarifying details
      (Harry Callahan)
    * Record test failure due to timeout in regr.log (Harry Callahan)
    * Update docs for (s/ms)context (Harry Callahan)
    * Update SCONTEXT address, add MSCONTEXT csr to match riscv_debug 1.0
      (Harry Callahan)
    * [pmp] Remove off mode from pmp_*_mode_cross coverpoints (Marno van
      der Maas)
    * [cosim] Fix spike cosim instruction count (Greg Chadwick)
    * [cosim] Pass Ibex config through for verilator cosim (Greg Chadwick)
    * [rtl] Don't cache instructions in debug mode (Greg Chadwick)
    * [rtl] Switch FF RF to use unpacked arrays (Greg Chadwick)
    * [dv] Fix timeout issues (Greg Chadwick)
    * [rtl] Add ic_scr_key_valid field to CPUCTRL (renamed CPUCTRLSTS)
      (Greg Chadwick)
    * [cosim] Pass SecureIbex and ICache paramters through to cosim (Greg
      Chadwick)
    * [doc] Bump privileged spec version to v1.12 (Greg Chadwick)
    * [rtl] Remove/reword comments referring to specific specifications
      (Greg Chadwick)
    * [rtl] Clear mprv on mret to non M-mode (Greg Chadwick)
    * [rtl, dv] Add new CSRs for latest priviledged spec (Greg Chadwick)
    * [dv] Prevent PMP setup for riscv_mem_error_test (Greg Chadwick)
    * Update google_riscv-dv to google/riscv-dv@9c2b007 (Greg Chadwick)
    * [dv] Increase generated CSR instructions in riscv_rand_instr_test
      (Greg Chadwick)
    * [cosim] Fix various CSR mismatches (Greg Chadwick)
    * [dv, cosim] Fix mcycle setting (Greg Chadwick)
    * [dv] Improve riscv_core_setting.sv template (Greg Chadwick)
    * [dv] Add makefile step for generating core config file from template
      (Greg Chadwick)
    * [rtl] Integrity errors only relevant to loads (Greg Chadwick)
    * [dv] Drive read data/integrity to X for write response (Greg
      Chadwick)
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
