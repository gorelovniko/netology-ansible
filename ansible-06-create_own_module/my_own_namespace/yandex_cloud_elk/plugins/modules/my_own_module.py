#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This module creates a text file with specified content

version_added: "1.0.0"

description: This module creates a text file at the specified path with the given content.

options:
    path:
        description: The path where the file should be created.
        required: true
        type: str
    content:
        description: The content to write to the file.
        required: true
        type: str
    mode:
        description: The permissions of the file.
        required: false
        type: str
        default: '0644'

author:
    - GorelovNN (@student)
'''

EXAMPLES = r'''
# Create a file with content
- name: Create a test file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "Hello World!"

# Create a file with specific permissions
- name: Create a secure file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/secure.txt
    content: "Secret content"
    mode: '0600'
'''

RETURN = r'''
path:
    description: The path of the created file.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content:
    description: The content that was written to the file.
    type: str
    returned: always
    sample: 'Hello World!'
mode:
    description: The permissions set for the file.
    type: str
    returned: always
    sample: '0644'
changed:
    description: Whether the file was changed.
    type: bool
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os
import tempfile


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
        mode=dict(type='str', required=False, default='0644')
    )

    result = dict(
        changed=False,
        path='',
        content='',
        mode=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    path = module.params['path']
    content = module.params['content']
    mode = module.params['mode']

    result['path'] = path
    result['content'] = content
    result['mode'] = mode

    try:
        # Check if file exists and content is the same
        file_exists = os.path.exists(path)
        content_changed = True
        
        if file_exists:
            with open(path, 'r') as f:
                existing_content = f.read()
            content_changed = existing_content != content
        
        if not file_exists or content_changed:
            # Create directory if it doesn't exist
            dir_path = os.path.dirname(path)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, mode=0o755)
            
            # Write file
            with open(path, 'w') as f:
                f.write(content)
            
            # Set permissions
            os.chmod(path, int(mode, 8))
            result['changed'] = True
        
        module.exit_json(**result)
        
    except Exception as e:
        module.fail_json(msg=f"Failed to create file: {str(e)}", **result)


def main():
    run_module()


if __name__ == '__main__':
    main()