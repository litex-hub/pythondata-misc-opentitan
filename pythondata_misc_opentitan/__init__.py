import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11185"
version_tuple = (0, 0, 11185)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11185")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11059"
data_version_tuple = (0, 0, 11059)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11059")
except ImportError:
    pass
data_git_hash = "e518af79866d138513af3b6394a6885abdbde78a"
data_git_describe = "v0.0-11059-ge518af798"
data_git_msg = """\
commit e518af79866d138513af3b6394a6885abdbde78a
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Mar 29 11:18:04 2022 -0700

    [dv/otp_ctrl] Fix stress_all_with_rand_reset seq
    
    This PR fixes otp_ctrl's stress_all_with_rand_reset:
    1). Method to force the mubi value - previous method try to use for
      loop, and pre-assign the mubi values to all partitions before forcing
      them. This will work for normal sequences but not
      stress_all_with_rand_reset. Because if the previous parition is not
      locked (force it to unlocked value), then next sequence lock it without reset(
      usually sequence will reset here), then next sequence cannot be locked
      because of the force value.
      So this PR change it to only force locked value to undeclared mubi
      values.
    2). In stress_all_with_rand_reset sequence, because reset we use a
      different task `apply_resets_concurrently`, it does not include all
      the overrides for `apply_reset` and `dut_init`. To adds the additional
      overrides, I used to put it under `otp_ctrl_stress_all_vseq`. However,
      stress_all_with_rand_reset is based on `common_sequence` instead, so
      this override did not apply to `stress_all_with_rand_reset` sequence.
      So I moved the override to base task.
    3). For the timing to re-enable scb: because in some fatal error user
      has to issue reset to get a functional OTP again, so
      stress_all_with_rand_reset child sequence will wait until reset is
      issue. If we enable the scb during post_start(), but did not issue
      reset immediately, scb will report error.
      The solution here is to move `en_scb` when apply_reset is issued.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
