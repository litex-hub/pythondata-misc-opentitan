import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8163"
version_tuple = (0, 0, 8163)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8163")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8051"
data_version_tuple = (0, 0, 8051)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8051")
except ImportError:
    pass
data_git_hash = "c720ac8dc602381144a67106995f974fa6cc75f5"
data_git_describe = "v0.0-8051-gc720ac8dc"
data_git_msg = """\
commit c720ac8dc602381144a67106995f974fa6cc75f5
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Wed Mar 3 15:34:53 2021 +0000

    [rv_plic] Produce top_earlgrey instance of rv_plic with ipgen
    
    This rather large commit makes rv_plic an IP template, and then uses
    ipgen to instantiate the block with the right parametrization for
    top_earlgrey.
    
    In contrast to the previous approach, `hw/top_earlgrey/ip_autogen`
    now contains a full copy of rv_plic under a unique FuseSoC core
    name, `lowrisc:opentitan:top_earlgrey_rv_plic`.
    
    Unfortunately, doing so requires a fair amount of reshuffling, which
    cannot be easily split into individual commits while keeping the whole
    tree building. Here's what was done:
    
    * Move `ip/rv_plic` to `ip_templates/rv_plic`.
    * Remove the `reg_rv_plic.py` tooling, which is now replaced by ipgen.
    * Change `topgen.py` to generate the toplevel-specific instance of
      `rv_plic` through ipgen.
    * Adjust references in the documentation as necessary.
    * Adjust the software build as necessary.
    * The FPV testbench is now only run for the Earl Grey-instantiated IP
      block, there is no more "generic" testbench. Update all references
      pointing to the testbench.
    
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
