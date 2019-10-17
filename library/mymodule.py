#!/usr/bin/python3


ANSIBLE_METADATA = {
    'metadata+version': '1.1',
    'status': ['preview'],
    'supported_by': 'rzfreeser'
    }

DOCUMENTATION = '''
---
module: mymodule
short_description: This module is being desigined so we can observe the minimum required config for an Ansible module.
version_added = "2.8"
description:
  - this module is being designed so we can observe the minimum required config for an ansible module
  - user passes a parameter called "name" <str> <required>
  - user passes a parameter called "augment: " <bool> <not required>
  - If augment: true then ansible returns the name value and additional string as well as indicates a YELLOW change on the PLAY RECAP
  - if augment: false then ansible returns name string and indicates a GREEEN OK on PLAY RECAP
  - if name: fail me then ansible returns FAILED in PLAY RECAP
author:
  rzfeeser@alta3.com
'''

EXAMPLE = '''
- name: this would get a green okay
  mymodule:
    name: Zach
    augment: false

- name: this would get a yellow change
  mymodule:
    name: Zach
    augment: true

- name: this would get a red fail
  mymodule:
    name: fail me
'''

RETURN = '''
original_message:
  description: the name param that was passed in by the user
  type: str
message:
  description: the name param the same way it was passed or the new augmented name param
  type: str
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    ## define the parameters that the user is allowed to pass in
    module_args = dict(
        name=dict(type='str', required=True),
        augment=dict(type='bool', default=False)
        )
    ## sed the return object
    result = dict(
        changed=False,
        original_message='',
        message=''
        )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
        )

    if module.check_mode:
        return result

    result['original_message'] = module.params['name']

    if module.params['augment'] == False:
        result['message'] = module.params['name']
    else:
        result['message'] = module.params['name'] + " is a wild and crazy guy!!! -- Dan Akroyd"
        result['changed'] = True

    if mdule.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    module.exit_json(**result)

def main():
   run_module()

if __name__ == "__main__":
    main()
