#!/usr/bin/env python

#############################
# Teflon
#############################
# Author:       Aaron Heath (aaron@aaronheath.com)
# URL:          https://github.com/aaronheath/teflon
# License:      MIT License (c) 2015 Aaron Heath
# Description:  A simple procedual python script to perform HTTP redirects.
#############################

import os
import cgitb
import re
import imp

c = imp.load_source('config', '../config.py')
config = c.config

cgitb.enable(display=not config["debug"], format="text")

## Let's get the env vars

env = os.environ

# Scheme

scheme = ""

if "REQUEST_SCHEME" in env:
    scheme = env['REQUEST_SCHEME']

if "SERVER_PORT" in env and scheme == "":
    scheme = "https" if env['SERVER_PORT'] == "443" else "http"

# Domain

domain = ""

if "HTTP_HOST" in env:
    domain = env['HTTP_HOST']

if "SERVER_NAME" in env and domain == "":
    domain = env['SERVER_NAME']

# Port

port = ""

if "SERVER_PORT" in env:
    port = "" if env['SERVER_PORT'] == "80" or env['SERVER_PORT'] == "443" else ":" + env['SERVER_PORT']

# Path and Query

pathAndQuery = ""

if "REQUEST_URI" in env:
    pathAndQuery = "/" if env['REQUEST_URI'] == "" else env['REQUEST_URI']

# Find matching redirection

fullRequest = scheme + "://" + domain + port + pathAndQuery
redirectTo = ""

for redirection in config["redirections"]:
    cre = re.compile(redirection["src"])
    mre = cre.match(fullRequest)
    redirectTo = redirection["dest"]
    break

# Perform redirection if not in debug mode

if not config["debug"] and redirectTo != "":
    print "Status: 301 Moved Permanently"
    print "Location: " + redirectTo

# Page content

print "Content-Type: text/plain;charset=utf-8"
print

if redirectTo != "":
    if not config["debug"]:
        print "Redirecting to " + redirectTo
    else:
        print "Would redirect to " + redirectTo

## Debug

if config["debug"]:
    # print env
    # print "\n"

    print "Scheme: " + scheme
    print "Domain: " + domain
    print "Port: " + port
    print "Path and Query: " + pathAndQuery
    print "Full Request: " + fullRequest
    print "Debug mode: " + str(config["debug"])