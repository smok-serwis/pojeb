# Pojeb

Pojeb is an extremely simplistic package manager. It has grown out of 
frustration at existing Python build tools, which obviously _cannot perform
the simple task of placing a fucking file at a particular directory_.

Forget automatically placing your _/etc/init.d_ scripts, even if you
are in total control of the environment!

You can do _virtualenv_, _wheel-based binary installs_, but you 
can't get your job done and go home. Fuck it all.

[Pythonrants](https://pythonrants.wordpress.com/) you right very much.

## Directory structure

* _/etc/pojeb/wyjeb.d/_ - fucking scripts that remove your shit, eg.
  * _/etc/pojeb/wyjeb.d/pojeb_ - script that removes **pojeb**
* _/bin/\*jeb_ - commands go here. If you don't like it, move'em. 

## Installation

Checkout the repo/unzip the zip with pojeb. Call `./install.sh` as root.
Done.

## Usage

* _dojeb your-package.jeb_ - install a package
* _wyjeb your-package_ - uninstall a package
* _przyjeb hostname@remotehost your-package.jeb_ - install a package on
  a remote machine'
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

# FAQ

Q: What should install/uninstall scripts be written in?

A: I don't care. They must have a shebang, pojeb will chmod +x them,
   and just run them. If it's available on your system, it's fair game.

---

Q: Why should I use pojeb?

A: Because it allows you to get your shit done and go home early, or 
   do more interesting things instead of trying to put your files
   somewhere.
