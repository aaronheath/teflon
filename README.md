# Teflon

A simple procedual python script to perform HTTP redirects.

### Summary

This script was developed as a quick effort to enable a number of my domains that were not being utilised to redirect to [my personal site](https://aaronheath.com/).

The solution is not designed to be ultra dynamic, hence does not use a database. Instead I have a single config file where a set of regular expression rules are tested against the supplied URL. If matched, a redirect to 'dest' is performed.

### Installation

The script was developed for an Apache 2.4 web server, so with that in mind ensure that the sites config has the following settings.

```
Options +ExecCGI
DirectoryIndex router.py
AddHandler cgi-script .py

RewriteEngine on
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule . router.py [PT,L]
```

Make sure that Apache modules mod_rewrite and mod_cgi are loaded.

You'll also need to make sure that the DocumentRoot is set to the 'public' subdirectory.

Supplied is an example configuration file (config.example.py), a new file config.py will need to be generated that obeys the same format and includes both 'debug' (bool) and 'redirection' (list) key values within the 'config' dictionary.

### The Future

This was a quick little script to get this up and running as quickly as possible however it's quite likely that I'll want / need to add features as time goes on.