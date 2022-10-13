import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14732"
version_tuple = (0, 0, 14732)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14732")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14590"
data_version_tuple = (0, 0, 14590)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14590")
except ImportError:
    pass
data_git_hash = "0681ffa10a42f151309530fc10511e284a76fc18"
data_git_describe = "v0.0-14590-g0681ffa10a"
data_git_msg = """\
commit 0681ffa10a42f151309530fc10511e284a76fc18
Author: Joshua Park <jeoong@google.com>
Date:   Thu Oct 6 16:32:59 2022 -0700

    [SPI_DEVICE|SPI_FLASH] Added a write-protection on en4b/ex4b to avoid SW overwrite
    
    - Issue : as reported in #14940, hhen CSB has a short deassertion time, the next sck_csb_asserted_pulse can show up at the next SPI transaction while the previous propagation is still ongoing. Since spi_reg_cfg_addr_4b_en_sync still shows the old value different from spi_cfg_addr_4b_en_o, spi_cfg_addr_4b_en_o is written again by the old value.
    - In this fix, the HW source-of-truth value is protected till its mirrorred SW regs is updated
    
    Signed-off-by: Joshua Park <jeoong@google.com>

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
