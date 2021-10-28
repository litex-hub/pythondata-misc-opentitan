import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8488"
version_tuple = (0, 0, 8488)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8488")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8376"
data_version_tuple = (0, 0, 8376)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8376")
except ImportError:
    pass
data_git_hash = "5e04deddd4b79a925fe031b8f212beafd7b2132a"
data_git_describe = "v0.0-8376-g5e04deddd"
data_git_msg = """\
commit 5e04deddd4b79a925fe031b8f212beafd7b2132a
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Wed Oct 27 22:55:59 2021 +0100

    Revert "[ spi_host ] Flag non-allowed write events as errors"
    
    This reverts commit 3193d73abd2f41dca02f376d70c0e070d7cfcec9.
    
    This commit broke private CI:
    
    ```
    * `UVM_ERROR (csr_utils_pkg.sv:466) [csr_utils::csr_rd_check] Check failed obs == exp (* [*] vs * [*]) Regname: chip_reg_block.spi_host*.error_status` has 1 failures:
        * Test chip_csr_rw has 1 failures.
            * 0.chip_csr_rw.1\
              Line 130, in log /azp/agent/_work/1/s/scratch/HEAD/chip_earlgrey_asic-sim-vcs/0.chip_csr_rw/out/run.log
    
                    UVM_ERROR @ 1081370000 ps: (csr_utils_pkg.sv:466) [csr_utils::csr_rd_check] Check failed obs == exp (8 [0x8] vs 0 [0x0]) Regname: chip_reg_block.spi_host1.error_status
                    UVM_INFO @ 1081370000 ps: (uvm_report_server.svh:901) [UVM/REPORT/SERVER]
                    --- UVM Report Summary ---
    
                    Quit count reached!
    ```
    
    The PR itself was green, so probably a mid-air collision.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
