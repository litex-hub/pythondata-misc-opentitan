import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12608"
version_tuple = (0, 0, 12608)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12608")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12466"
data_version_tuple = (0, 0, 12466)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12466")
except ImportError:
    pass
data_git_hash = "02b2c0a6067cc654457be84ec5faa6ea8e8bdcbc"
data_git_describe = "v0.0-12466-g02b2c0a60"
data_git_msg = """\
commit 02b2c0a6067cc654457be84ec5faa6ea8e8bdcbc
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Tue May 24 14:21:19 2022 -0700

    [opentitantool]: Allow SPI chip select across transactions
    
    While implementing TPM communication, I came across a use case in which
    I wanted to perform a few SPI transfers, inspect the data that was read,
    and then possibly issue some more SPI transfers, while keeping CS
    asserted throughout.
    
    The current `spi::Target` interface is such that `run_transaction()`
    keeps CS asserted for the duration of the list of transfers given in the
    parameter list and then deasserts it unconditionally, with no option to
    add more based on the result of the previous ones.
    
    This PR introduces an explicit `assert_cs()` function, which can be used
    to keep CS asserted across multiple invocations of `run_transaction()`,
    like below.
    
    ```
    let spi = ...;
    {
      let _cs_asserted = spi.assert_cs()?;
      spi.run_transaction(...)?;
      if ... {
        spi.run_transaction(...)?;
      }
      // CS will automatically deassert here (or earlier if bailing out.)
    }
    ```
    
    Furthermore, `assert_cs()` counts its invocations, and releases CS only
    when every nested assertion has been released, such that if the above
    code was part of a helper method, and the called wanted to make several
    invocations of the helper, during a single CS session, then it could put
    another `assert_cs()` around its logic.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: I219f3647d29129c4dfc1fc346f855fb4e9da2e53

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
