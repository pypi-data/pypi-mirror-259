# Author: Scott Woods <scott.18.ansar@gmail.com.com>
# MIT License
#
# Copyright (c) 2022, 2023 Scott Woods
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""".

.
"""
__docformat__ = 'restructuredtext'

__all__ = [
	'BlankSettings',
	'DirectorySettings',
	'procedure_blank',
	'procedure_directory',
]

import sys
import os
import stat
import signal
import errno
import datetime
import calendar
import tempfile
import uuid
import re
import ansar.create as ar
from ansar.create.procedure import DEFAULT_HOME, DEFAULT_GROUP, HOME, GROUP
from ansar.create.procedure import open_home, open_role, role_status
from .directory import *


# Per-command arguments as required.
# e.g. command-line parameters specific to create.
class BlankSettings(object):
	def __init__(self,
			home_path=None,
			redirect_bin=None,
			redirect_lock=None,
			redirect_settings=None,
			redirect_logs=None,
			redirect_resource=None,
			redirect_tmp=None,
			redirect_model=None
			):
		self.home_path = home_path
		self.redirect_bin = redirect_bin
		self.redirect_lock = redirect_lock
		self.redirect_settings = redirect_settings
		self.redirect_logs = redirect_logs
		self.redirect_resource = redirect_resource
		self.redirect_tmp = redirect_tmp
		self.redirect_model = redirect_model

BLANK_SETTINGS_SCHEMA = {
	'home_path': ar.Unicode(),
	'redirect_bin': ar.Unicode(),
	'redirect_lock': ar.Unicode(),
	'redirect_settings': ar.Unicode(),
	'redirect_logs': ar.Unicode(),
	'redirect_resource': ar.Unicode(),
	'redirect_tmp': ar.Unicode(),
	'redirect_model': ar.Unicode(),
}

ar.bind(BlankSettings, object_schema=BLANK_SETTINGS_SCHEMA)

#
#
class DirectorySettings(object):
	def __init__(self, group_name=None, home_path=None, directory_scope=None, connect_above_file=None):
		self.group_name = group_name
		self.directory_scope = directory_scope
		self.home_path = home_path
		self.connect_above_file = connect_above_file

DIRECTORY_SETTINGS_SCHEMA = {
	'group_name': ar.Unicode(),
	'home_path': ar.Unicode(),
	'directory_scope': ScopeOfService,
	'connect_above_file': ar.Unicode(),
}

ar.bind(DirectorySettings, object_schema=DIRECTORY_SETTINGS_SCHEMA)

#
#
def procedure_blank(self, blank):
	return None

#
#
def procedure_directory(self, directory, group, home):
	group = ar.word_argument_2(group, directory.group_name, DEFAULT_GROUP, GROUP)
	home = ar.word_argument_2(home, directory.home_path, DEFAULT_HOME, HOME)

	if '.' in group:
		e = ar.Rejected(group_name=(group, f'no-dots name'))
		raise ar.Incomplete(e)
	group_role = f'group.{group}'

	hb = open_home(home)

	_, running = role_status(self, hb, [group_role])
	if running:
		e = ar.Failed(group_start=(f'group "{group}" is already running', None))
		raise ar.Incomplete(e)

	settings = []
	if directory.directory_scope:	# Explicit level.
		s = ScopeOfService.to_name(directory.directory_scope)
		settings.append(f'--directory-scope={s}')

		# Assignment of new connection.
		if directory.connect_above_file:
			settings.append(f'--connect-above-file={directory.connect_above_file}')

	elif directory.connect_above_file:
		e = ar.Rejected(connect_with_no_scope=('missing scope', None))
		raise ar.Incomplete(e)

	else:	# Default lookup to the top.
		s = ScopeOfService.to_name(ScopeOfService.WAN)
		settings.append(f'--directory-scope={s}')

	try:
		a = self.create(ar.Process, 'ansar-group',	
					origin=ar.START_ORIGIN,
					home_path=hb.home_path, role_name=group_role, subrole=False,
					settings=settings)

		# Wait for Ack from new process to verify that
		# framework is operational.
		m = self.select(ar.Completed, ar.Stop)
		if isinstance(m, ar.Stop):
			# Honor the slim chance of a control-c before
			# the framework can respond.
			self.send(m, a)
			m = self.select(ar.Completed)

		# Process.
		value = m.value
		if isinstance(value, ar.Ack):	   # New instance established itself.
			pass
		elif isinstance(value, DirectoryAncestry):
			return value
		elif isinstance(value, ar.Faulted):
			raise ar.Incomplete(value)
		elif isinstance(value, ar.LockedOut):
			e = ar.Failed(role_lock=(None, f'"{group_role}" already running as <{value.pid}>'))
			raise ar.Incomplete(e)
		else:
			e = ar.Failed(role_execute=(value, f'unexpected response from "{group_role}" (ansar-group)'))
			raise ar.Incomplete(e)
	finally:
		pass

	return None
