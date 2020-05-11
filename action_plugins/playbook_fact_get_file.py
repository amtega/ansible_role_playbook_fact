# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
import sys
from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    TRANSFERS_FILES = False

    def get_file(self):
        """Return playbook file.

        Returns:
            str: playbook file name.
        """
        # Setup argument parser

        for arg in sys.argv:
            if re.search(r'.*\.ya?ml', arg):
                file = arg
                break

        return file

    def run(self, tmp=None, task_vars=None):
        """Ansible action plugin main run method."""

        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        result['changed'] = False
        result['failed'] = False
        result['file'] = self.get_file()

        return result
