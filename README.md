# hashword

## Installation

```shell
pip install hashword
```

On Linux you will need xclip, which is required by [https://github.com/asweigart/pyperclip](Pyperclip).

Ubuntu
```shell
sudo apt-get install xclip
```

## Usage

- Run hashword with an identifier for a service
- Enter your master password.
- Paste your password.

```shell
hashword service1
Master Password: <masterpassword>
Password copied to clipboard.
```

For example I entered ```master``` when prompted and ```ea121fccac3b544da1ac2d05510d2d9898ca09d5c1fa71241075a2723809a36a``` was added to the clipboard.

## What is my master password?

Your master password is anything you want. This is the last password you need to remember.

It is not stored and will not be verified when entered. If you want to change your master password simply start using your new master password.

## How does it work?

The argument you pass hashword and your master password are combined and used as input to the SHA256 hash function.
The result is your password.

## What should I do when a service I used is hacked?

Create a new password with a different service identifier.

If the password database is compromised, an attacker can get access to your password. If your password was stored in plaintext then the attacker knows the long string you paste as your password.

The attacker would also need to know this was created using SHA256. Then they would try common inputs and eventually the set of all inputs for all characters.

If the password was not stored as plaintext then they would have to do that twice.

In order for your other passwords on other sites to be comprised they would have to figure out your other site identifiers and hash them with your master password.
