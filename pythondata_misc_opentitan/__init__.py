import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14920"
version_tuple = (0, 0, 14920)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14920")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14778"
data_version_tuple = (0, 0, 14778)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14778")
except ImportError:
    pass
data_git_hash = "05660af1ea0847569bd4703995a9c0a78008f6c2"
data_git_describe = "v0.0-14778-g05660af1ea"
data_git_msg = """\
commit 05660af1ea0847569bd4703995a9c0a78008f6c2
Author: Dan McArdle <dmcardle@google.com>
Date:   Fri Oct 21 16:52:23 2022 -0400

    [bazel] Rewrite GDB test script, respect subprocess exit codes
    
    To implement #14490, we'll want to assert that the value of PC is the
    address of a particular function. GDB is in a perfect position to test
    this kind of assertion. It knows the addresses of symbols, it knows the
    values of registers, it supports conditional expressions, and it has a
    `quit` command, which takes an exit code parameter.
    
    When I tried inserting an unconditional `quit 123` into the existing GDB
    script for sram_program_fpga_cw310_test, I was surprised that the test
    did not fail! It turns out we have been silently ignoring exit codes of
    background processes.
    
    I decided to rewrite the test script in Python, if only for clarity. The
    rewrite is nearly a drop-in replacement. The only intentional difference
    is that it checks the exit codes of its subprocesses.
    
    As a proof of concept, I inserted these lines into the GDB script for
    sram_program_fpga_cw310_test and verified that it works as expected:
    
    ```
            if &sram_main == 0x10001fc5
              echo :::: Correct.\\n
            else
              echo :::: Surprise!\\n
              quit 123
            end
    ```
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
