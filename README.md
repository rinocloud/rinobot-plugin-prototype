# rinobot-plugin-prototype

This is a prototype structure for a rinobot plugin.

- [Installation](#installation)
- [Configuration](#configuration)
- [Programming your plugin](#programming-your-plugin)
- [Deploying your plugin](#deploying-your-plugin)

## Installation

- [Download this repository](https://github.com/rinocloud/rinobot-plugin-prototype/archive/master.zip)

- or clone it `git clone https://github.com/rinocloud/rinobot-plugin-prototype.git`

First you will need python3 installed, we recommend the Anaconda Python 3
distribution because its what we require Rinobot users to install, it contains a
large number of useful scientific libraries like numpy, scipy and matplotlib by
default.

- [Anaconda Python](https://www.continuum.io/downloads) install Python 3
- [List of default packages](https://docs.continuum.io/anaconda/pkg-docs)

## Configuration

You will need to install node.js and npm, and make an NPM account in order to publish your plugin
to the npm package directory.

- [Node & NPM installation](https://nodejs.org/en/download/current/)
- [Create an npm account](https://www.npmjs.com/signup)

### The package.json file

This is the file which holds all the configuration for your rinobot plugin

Inside the `package.json` you will need to:

1. prefix the package name with `rinobot-plugin-`

2. include the keyword `rinobot`

Most of this is done for you already in this prototype repo, but you'll need to change
the package name and user, and version

## Programming your plugin

To make your own plugin just start editing the `index.py` file in python. You
can import all the [default packages installed by
Anaconda](https://docs.continuum.io/anaconda/pkg-docs).

Also its good to keep details documentation of how your plugin behaves in this
README.md file.

## Deploying your plugin

If your happy with your plugin: just type

```bash
npm version patch
```
to create a new version, use `patch`, `minor`, or `major` in accordance with [semver](http://semver.org/).
Then to publish to the package registry just type:

```bash
npm publish
```

Your plugin will be available in Rinobot.

We also recommend you version control your plugin with `git` and host the repository on [github](https://github.com).
