# ansible-role-authorized-principals

A simple ansible role to manage authorized principals files.

## Requirements

This role has no requirements.

## Role Variables


| Name                        | Default                    | Descriptions                                                 |
|-----------------------------|----------------------------|--------------------------------------------------------------|
| `authorized_principals_dir` | `/etc/ssh/auth_principals` | Directory into which to save the authorized principals files |

## Dependencies

This role has no dependencies.

## Example Playbook

```yaml
- hosts: all
  roles:
    - pmeyerra.authorized_principals
```

## Tests

Testing is done using `molecule` and `Testinfra`.

The test pip dependencies can be installed using the command below.

```bash
pip install ansible molecule[docker] docker pytest-testinfra
```

## References

The great [`geerlingguy.docker`](https://github.com/geerlingguy/ansible-role-docker) 
role gave me some inspiration for the structure of this role. Also
[this](https://www.jeffgeerling.com/blog/2018/testing-your-ansible-roles-molecule) 
blog post from Jeff Geerling was very helpful.