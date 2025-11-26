# Ansible Collection - my_own_namespace.yandex_cloud_elk

Documentation for the collection.

# My Own Namespace - Yandex Cloud ELK Collection

This collection contains custom modules and roles for managing Yandex Cloud ELK stack.

## Modules

### my_own_module

Creates a text file with specified content on remote hosts.

## Roles

### create_file

Role that uses my_own_module to create files with configurable parameters.

## Installation

```bash
ansible-galaxy collection install my_own_namespace.yandex_cloud_elk
```

## Usage

```yml
- name: Create file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: "/tmp/example.txt"
    content: "Hello World!"
    mode: '0644'
```