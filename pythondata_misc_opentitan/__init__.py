import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5663"
version_tuple = (0, 0, 5663)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5663")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5568"
data_version_tuple = (0, 0, 5568)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5568")
except ImportError:
    pass
data_git_hash = "a753d34a477855925ce634d02e9d7445411b629c"
data_git_describe = "v0.0-5568-ga753d34a4"
data_git_msg = """\
commit a753d34a477855925ce634d02e9d7445411b629c
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Mon Mar 22 14:08:15 2021 +0000

    [dif_kmac] Add header file and checklist for KMAC DIF.
    
    This API provides a streaming interface to the KMAC unit. The KMAC
    unit will be initialized with information about how entropy will be
    generated and the endianness of the message and digest. After that
    a transaction can be started by passing the required information
    (e.g. key) to a `dif_kmac_mode_{sha3,shake,cshake,kmac}_start`
    function. Data is then passed into the hash function using the
    `dif_kmac_absorb` function. Once the data to be hashed has been
    completely absorbed the output (a.k.a. digest) can be written out
    using the `dif_kmac_squeeze` function. The output may be a variable
    or fixed length depending on the mode. Once the squeeze has been
    started no further absorb operations can be performed. Finally,
    `dif_kmac_end` is called to end the operation ready for a new
    operation to be started.
    
    Example:
    
    ```c
    // Initial hardware configuration.
      dif_kmac_config_t config = (dif_kmac_config_t) {
        .entropy_mode = kDifKmacEntropyModeSoftware,
        .entropy_seed = generate_seed(),
        .entropy_fast_process = kDifKmacToggleEnabled,
        .message_endianness = kDifKmacEndiannessLittle,
        .output_state_endianness = kDifKmacEndiannessLittle,
      };
      CHECK(dif_kmac_configure(&kmac, config));
    
      // Example KMAC XOF calculation with empty customization string.
      CHECK(dif_kmac_mode_kmac_start(&kmac,
                                     0 /* L=0 (XOF) */,
                                     &key,
                                     nullptr /* S="" */));
      CHECK(dif_kmac_absorb(&kmac, msg, len, nullptr /* block */));
      CHECK(dif_kmac_squeeze(&kmac, out, len, nullptr /* block */));
      CHECK(dif_kmac_end(&kmac));
    ```
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
