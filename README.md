# unopass

##### Written by [Amado Tejada](https://www.linkedin.com/in/amadotejada/)

##
*unopass* is a convenient python module that allows you to retrieve secrets from the 1Password CLI at runtime using your biometrics.

This eliminates the need of storing secrets in env, or conf files and provides a more secured local workflow.
##

<img src="https://i.ibb.co/7V3vCB0/gif.gif" width="100%">

Note: *unopass* is early alpha software and should be tested extensively.

#### Requirements:
 * [ 1Password CLI ](https://developer.1password.com/docs/cli/get-started#install) v2.4.1 or higher
 * [ 1Password App ](https://1password.com/downloads/) v8.7.1 or higher
 *  [Biometrics](https://developer.1password.com/docs/cli/get-started#turn-on-biometric-unlock) enabled

### Security
Authorization expires after 10 minutes of inactivity in the session. There's a hard limit of 12 hours, after which you must reauthorize.

Learn about 1Password Biometrics [Security](https://developer.1password.com/docs/cli/biometric-security)

### Install

[pypi repo](https://pypi.org/project/unopass/):
```bash
pip3 install unopass
```

You can also import *unopass* from source.

### Example

```python
from unopass import unopass as secret


"""
secret.unopass({VAULT}, {ITEM}, {FIELD})

OPTIONAL: signout of the 1Password CLI session:
    call secret.signout() with deauthorize=True to end of the 1Password session
"""

username = secret.unopass("personal", "server", "username")
password = secret.unopass("personal", "server", "password")

secret.signout(deauthorize=True)


print(f"user: {username}\npass: {password}")
```

##
### Disclaimer

This software {*unopass*} has not been endorsed or supported by 1Password, AgileBits Inc. and is in no way associated with them and/or its subsidiaries or affiliate.

### License

*unopass* is released under the [MIT License](https://github.com/amadotejada/unopass/blob/main/LICENSE)
####
