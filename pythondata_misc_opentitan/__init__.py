import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10820"
version_tuple = (0, 0, 10820)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10820")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10694"
data_version_tuple = (0, 0, 10694)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10694")
except ImportError:
    pass
data_git_hash = "a6f0f3a4c6b80ccfea7bc8462d0797267bef5d22"
data_git_describe = "v0.0-10694-ga6f0f3a4c"
data_git_msg = """\
commit a6f0f3a4c6b80ccfea7bc8462d0797267bef5d22
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Mar 9 13:19:22 2022 -0800

    [chip dv] Add AST initialization routine
    
    This commit adds the initialization routine to:
    - Backdoor load the AST configuration partion in OTP with data that will
      be read by the test/mask ROM and written to the AST rega registers,
      for the SW tests
    
    - Do the same for non-SW tests, but also manually write the AST
      registers via the TLUL interface in dut_init(), before the tests
      begin.
    
    - This AST cfg data is added to chip_env_cfg, which can either be set to
      the correct values in the closed source extended partner_chip_env_cfg,
      or it can be set via plusarg.
    
    - The chip_base_test is updated to be templated, so that it can be
      overridden with a custom extension of chip_env_cfg, that can house the
      correct programming data for AST.
    
    This is an alternate approach to the PR #11275.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
