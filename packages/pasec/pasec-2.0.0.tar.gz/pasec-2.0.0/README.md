# PaSec
PaSec is a secure password generator that allows you to create strong, unique passwords using a passphrase of your choice. With PaSec, you can generate passwords that are virtually impossible to crack, giving you peace of mind when it comes to online security. It ensures that the generated password is always the same for a given passphrase.It will generate the strong password from weak passphrase which is easy to remember.

## Overview

This is Python library provides a function for generating strong passwords based on the user specified passphrase and length, and character composition CSSN(capital letters, small letters, symbols, and numbers). This is python library adaptation of web version of PaSec.
### Web Version => [pasec.ssuroj.com.np](https://pasec.ssuroj.com.np/)

## Installation

You can install the library via pip:

```bash
pip install pasec
`````

## Usage Example

To generate a strong password using the `PaSec()` function, follow these steps:

1. Import the `PaSec` function from the library:

    ```python
    from pasec import PaSec
    `````

2. Call the `PaSec` function with the following parameters:

    - `passphrase`: The passphrase used for generating the password.
    - `length` (optional): The desired length of the password (default is 20).
    - `cssn` (optional): A binary string specifying whether to include capital letters, small letters, symbols, and numbers in the password. Use '1' to include and '0' to exclude. The default is '1111' (i.e., include all).

    ```python
    # Example usage
    password = PaSec("mysecret", 20, "1101")
    # Now the password is saved in variable which can be used
    `````

In this example:
- The passphrase is "mysecret".
- The desired password length is 20 characters.
- The CSSN parameter "1101" specifies that the password should include capital letters, small letters, and numbers, but exclude symbols.


    ````
    ````
````
