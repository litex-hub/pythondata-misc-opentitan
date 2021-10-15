import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8294"
version_tuple = (0, 0, 8294)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8294")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8182"
data_version_tuple = (0, 0, 8182)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8182")
except ImportError:
    pass
data_git_hash = "d88e5c3daefc64d094ca4407e002a3499ad8cf6f"
data_git_describe = "v0.0-8182-gd88e5c3da"
data_git_msg = """\
commit d88e5c3daefc64d094ca4407e002a3499ad8cf6f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Oct 1 16:38:11 2021 +0100

    [otbn,dv] Sort out timing for done/status signals in ISS
    
    Now that otbn_core_model exposes a STATUS register, we can use it to
    derive the "done" signal. Using the status register directly, rather
    than reconstructing it from the done signal, models the OTBN block
    more closely and actually simplifies a load of tracking DV
    code (mainly because the two things that we're comparing Just Match,
    so we don't need to convert between the two views of the world).
    
    Unfortunately, we can't get rid of the "done" signal entirely, because
    otbn.sv can choose to instantiate the model instead of the RTL to
    represent the core. The timing isn't *quite* right here, because the
    core flops STATUS but not its done_o output. But this shouldn't matter
    for the chip-level sims where we use the model like this.
    
    We *do* check that the RTL's done signal is as predicted in the UVM
    and verilator testbenches.
    
    This patch also sorts out the timing of the start of execution in the
    UVM testbench: the ISS was probing the wrong start signal, so started
    a cycle late. This didn't matter too much, because it and the design
    were both waiting on the EDN, which took more than one cycle.
    
    Finally, we fix the assertion that checks the model and RTL have
    matching STATUS. This was broken before (using "rst_n", rather than
    "!rst_n"), which is why we didn't notice the off-by-one at the start.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
