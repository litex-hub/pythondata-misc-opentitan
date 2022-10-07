import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14613"
version_tuple = (0, 0, 14613)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14613")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14471"
data_version_tuple = (0, 0, 14471)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14471")
except ImportError:
    pass
data_git_hash = "144e5112df44eecab06d510455a77435551946a7"
data_git_describe = "v0.0-14471-g144e5112df"
data_git_msg = """\
commit 144e5112df44eecab06d510455a77435551946a7
Author: Weicai Yang <weicai@google.com>
Date:   Wed Oct 5 23:00:18 2022 -0700

    [spi_device] Add tpm_all test
    
    This test has the following sequence
    - Configure `TPM_CFG.EN` to On and fully randomize other TPM configuration.
    - Run these 3 threads to randomly access TPM HW registers and other addresses.
    - Host issues random TPM reads/writes to spi_device.
    - SW polls the TPM interrupt `tpm_header_not_empty`, then read command/address and
    the corresponding FIFO.
     - SW randomly updates TPM HW registers.
    - Ensure all the data is correct in the scoreboard.
    
    Also fix some small issues in the scb
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
