# Pojeb

Pojeb is an extremely simplistic package manager. It has grown out of 
frustration at existing Python build tools, which obviously _cannot perform
the simple task of placing a fucking file at a particular directory_.

Forget automatically placing your _/etc/init.d_ scripts, even if you
are in total control of the environment!

You can do _virtualenv_, _wheel-based binary installs_, but you 
can't get your job done and go home. Fuck it all.

[Pythonrants](https://pythonrants.wordpress.com/) you right very much.

Install via the ninja one-liner:

`wget -O - https://github.com/smok-serwis/pojeb/raw/master/jebac-to | sudo bash`

Requires _Python 2.x_, _sudo_, _wget_, _bash_, _tar_, _gzip_ and **root access**.
You don't have those? What are you running? Maybe not _fuck you_, but
a _shame on you_ certainly.

# When do I use it?

When you exact total control over your environment, because your layers
of abstraction consist of containers and VMs, and not _fucking virtualenvs_.

And you're not afraid of executing commands as root via shell, because you've
automated the fuck out of it, and your cluster is predictable, and not fucking
every VM has different distro of different version.

Fuck it, if your project requires sideloading 3 different versions of the same
package, then you're doing it wrong. Heartfelt **fuck you** for you.

## Directory structure

Name of the package is encoded in jebfile. If it's named **fuck-you.jeb**, 
then the name of the package is **fuck-you**.

* _/etc/pojeb/wyjeb.d/_ - fucking scripts that remove your shit, eg.
  * _/etc/pojeb/wyjeb.d/pojeb_ - script that removes **pojeb**
* _/bin/\*jeb_ - commands go here. If you don't like it, move'em. 

## Installation

### The one-liner ninja way

`wget -O - https://github.com/smok-serwis/pojeb/raw/master/jebac-to | sudo bash`

### The absolutely worst way

Checkout the repo/unzip the zip with pojeb. Call `./install.sh` as root.
Done.

## Usage

* _sudo dojeb your-package.jeb_ - install a package
* _sudo wyjeb your-package_ - uninstall a package
* _przyjeb username@remotehost your-package.jeb_ - install a package on
  a remote machine. If pojeb is not there already, it will be transparently installed
  via the ninja one-liner. **ssh** is 
  obviously required, and **sudo** must be callable on the target.
* _zajeb your-package_ - make a .jeb package file from a directory 
  called your-package. This will result in a _your-package.jeb_ file.

  
## How do I make pojeb packages

Let's say your are making a package called **fuck-you**. You should
make a directory called _fuck-you_. 

Everything here will get zipped when you call _zajeb_. Files with
special meaning are listed below.

### dojeb

A script (with a shebang!) that installs your package. This is called
as root, with the working directory of **fuck-you**. Pojeb will unzip
the .jeb file somewhere, chdir there and call _dojeb_. You just install
shit.

You should return exit code 0. Otherwise, installation will be
considered _failed_.

This should check if you are updating your own package. A good
way to check it is checking for existence of 
_/etc/pojeb/wyjeb.d/fuck-you_. 


**This does not have to copy wyjeb. Pojeb will take care of that**

### wyjeb

After successful installation this is moved to _/etc/pojeb/wyjeb.d_, 
in this case as _/etc/pojeb/wyjeb.d/fuck-you_.
This is a script that removes your package. It gets called when you do
_wyjeb fuck-you_. 

**This does not have to remove /etc/pojeb/wyjeb.d/fuck-you. Pojeb
will take care of that**

**If you don't put this file**, then your package will be un-uninstallable,
and _wyjeb_ command will cry if you try to remove it.

# FAQ

Q: What should install/uninstall scripts be written in?

A: I don't care. They must have a shebang, pojeb will chmod +x them,
   and just run them. If it's available on your system, it's fair game.

---

Q: Why should I use pojeb?

A: Because it allows you to get your shit done and go home early, or 
   do more interesting things instead of trying to put your files
   somewhere.

# lol wut
If you made it this far, then you know everything about pojeb there
is to know. If you feel you need to know something else, file a
bug report. Use the Issues tab for it. _Thank your for contributing_.
