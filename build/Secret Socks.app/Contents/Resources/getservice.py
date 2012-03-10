#!/usr/bin/env python
#
#  getservice.py
#  Determine the active network service name
#
#  Created by Joshua Chan on 09-09-03.
#

import os
import re

# Make a list of all available service names
fh = os.popen("networksetup -listnetworkserviceorder 2> /dev/null", "r")
services = []
for line in fh.readlines():
	m = re.search('^\(\d{1,2}\) ([\w -]+)$', line)
	if m:
		result = m.group(1)
		services.append(result)
fh.close()

# Find the first service with a router address
for service in services:
	fh = os.popen("networksetup -getinfo '%s'  2> /dev/null" %  service, "r")
	info = fh.read()
	fh.close()
	
	m = re.search('^Router: ', info, re.MULTILINE)
	if m:
		activeService = service
		break

print activeService
