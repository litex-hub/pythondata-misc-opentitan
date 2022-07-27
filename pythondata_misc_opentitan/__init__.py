import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13293"
version_tuple = (0, 0, 13293)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13293")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13151"
data_version_tuple = (0, 0, 13151)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13151")
except ImportError:
    pass
data_git_hash = "3345f7d4285d33ae4237ed76fe0d4e2fb17631c4"
data_git_describe = "v0.0-13151-g3345f7d428"
data_git_msg = """\
commit 3345f7d4285d33ae4237ed76fe0d4e2fb17631c4
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Tue Jul 19 12:00:25 2022 +0200

    [otbn,rtl,dv] Replace zeroing in secure wipe with writing random data
    
    As reasoned in #13499, the second round of a secure wipe should not
    write zeroes but PRNG-provided values.  This should make FI attacks that
    rely on a known (or even zero) register state much more difficult.
    Before that second round using PRNG-provided values, the PRNG has to be
    reseeded.  This is needed so the PRNG state that provided the values for
    the first wipe cannot be inferred from reading out registers after the
    wipe.
    
    This commit adds an URND reseed between the two rounds of a secure wipe
    and changes the second round from zeroing to using URND-provided values,
    like the first round.  This is mainly implemented in
    `otbn_start_stop_control`, which controls the secure wipe.
    Additionally, the bignum ALU and MAC are slightly modified as follows:
    - In `otbn_alu_bignum`, the `sec_wipe_zero_i` input is no longer used to
      zero the `MOD` register.  It is still used to zero the flags, though.
    - In `otbn_mac_bignum`, the `sec_wipe_zero_i` input has been removed.
      The MAC only used that input to zero the `ACC` register, which no
      longer happens.
    
    This commit also extends the number of cycles the start/stop FSM is
    allowed to take between an escalation and becoming locked from to 400
    (from 100), which is checked by two assertions in `otbn_core`.
    
    On OTBN DV, this commit makes the following changes:
    - Extend `otbn_core_model`, which models the URND request, to perform
      the URND reseed between the two rounds of a secure wipe.  This
      significantly increases the complexity of that part of the model, but
      the behavior is still coded independently from RTL (except the number
      of cycles for one wipe round, which is dictated by the RTL).
    - Change `otbn_scoreboard` to wait for an expected alert for up to 400
      cycles (instead of 150), as the URND reseed in the middle of a secure
      wipe potentially delays the raising of an alert.
    - Similarly, change `otbn_base_vseq` to wait for up to 500 cycles
      (instead of 300) for the initial secure wipe to complete and
      `otbn_intg_err_vseq` to wait up to 400 cycles (instead of 100) for
      OTBN to become locked after an injected integrity error.
    - Modify the registers in `otbnsim` to be *invalid* after a secure wipe.
      This is required because the registers are no longer zero after the
      secure wipe, yet the simulator does not know the random values written
      during secure wipe.
    - Modify and extend the `_step_wiping()` function of `otbnsim` to model
      two rounds of secure wipe with an URND refresh between them.
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
