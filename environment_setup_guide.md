This document is basically a short tutorial on how to get the server up and running. The only requirements are `python` (2.x) and `flask` to be installed.
This will cover linux and OSX, python on windows requires a bit more setup with setting environment variables - but it's easily google-able and easy to do.

# OS X

## Python

This section assumes that you have homebrew installed - if you don't please see this: http://brew.sh/#install You might also need to add `export PATH=/usr/local/bin:/usr/local/sbin:$PATH` in your `~/.profile` file. Once you have that:

To install python run:

    `$ brew install python`
    
That's... it. Verify that you have the right version of python installed by running `$ python --version` and you should see `Python 2.7.X`. You might also want to verify that you're running python you just installed and not the one that comes by default with OS X by running `$ which python` and that should tell you that it's using python from `/usr/local/bin/python`

# Linux

## Python

The chances are that you already have python installed. Just run `$ python --version` and make sure it's the latest `Python 2.7.X` version. In case you don't have python installed install it using your package manager e.g. `apt get install python` and verify the instalation is done by using the same command again.

# Flask - OSX/Linux

By installing python `pip` (the python package manager) will also be installed (if not, then google for OS specific instructions on how to install it).

To install flask on any operating system open your terminal/cmd and run `$ pip install flask` (it might ask for sudo permission in some cases). That's it, it will be installed.

# Running the server

Now that you have python and flask installed you can simply navigate to the folder where the `taskapp.py` file is and run it by executing `$ python testapp.py` and you will get an output that looks like this:

```
    $ python testapp.py                                                                                              
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You cna now open http://127.0.0.1:5000/ and see the initial dashboard page with the table.