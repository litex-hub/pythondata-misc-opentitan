import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14250"
version_tuple = (0, 0, 14250)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14250")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14108"
data_version_tuple = (0, 0, 14108)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14108")
except ImportError:
    pass
data_git_hash = "2fb276797e0dcda96195b1e4617f2aac82a925f0"
data_git_describe = "v0.0-14108-g2fb276797e"
data_git_msg = """\
commit 2fb276797e0dcda96195b1e4617f2aac82a925f0
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Sep 9 12:20:00 2022 -0700

    [sw] Add spi_host_tx_rx_test
    
    Add a basic spi host tx rx test.
    This test uses the spi_agent's native "loopback" behavior.
    The spi agent, when in device mode, by default just plays
    back whatever data is sent to it by the host.
    
    The test prepares a random payload, sends it to the device agent,
    and just reads back to make sure the data is matched.
    
    This test DOES NOT do any kind of flash protocol checking.
    
    - Add a device value for high speed peripehral clock
    - Add a minor fix for dif_spi_host clock divider setting
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [sw] test updates
    
    - update spi_host_tx_rx_test
    - minor fix for spi_host clock divider
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [dv] Add test sequence
    
    - updates to testplan
    - add if_mode setup into chip_base_test
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top/dv] Minor updates
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top/dv] spi_host configuration fix
    
    spi host does not support outputting at 1:1 frequencies.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top/dv] Various updates for spi_host testing
    
    - integrate with latest chip_if
    - add support for multiple spi_device agents
    - add enum to access pad pull-up attributes
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
