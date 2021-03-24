import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5573"
version_tuple = (0, 0, 5573)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5573")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5478"
data_version_tuple = (0, 0, 5478)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5478")
except ImportError:
    pass
data_git_hash = "5e75c8a3b08a6eab05d7bc71e3d7bfbc761ec94f"
data_git_describe = "v0.0-5478-g5e75c8a3b"
data_git_msg = """\
commit 5e75c8a3b08a6eab05d7bc71e3d7bfbc761ec94f
Author: Hoang Tung <Hoang.Tung@wdc.com>
Date:   Tue Mar 9 17:10:39 2021 -0800

    [spi_host, dv] Add baseline DV for csr_test
    
      - add spi_host_agent (device mode)
      - add env dv supports *csr tests
      - add tb.sv with 2 independent clock and reset sources
      - add spi_host_testplan.hjson to the list in build_docs.py script
    
    Signed-off-by: Hoang Tung <Hoang.Tung@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
