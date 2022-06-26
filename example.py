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
