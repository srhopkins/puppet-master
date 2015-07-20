#!/usr/bin/env python
import yaml
from sys import exit, argv

def construct_ruby_object(loader, suffix, node):
    return loader.construct_yaml_map(node)

def construct_ruby_sym(loader, node):
    return loader.construct_yaml_str(node)

yaml.add_multi_constructor(u"!ruby/object:", construct_ruby_object)
yaml.add_constructor(u"!ruby/sym", construct_ruby_sym)

try:
    with open('/var/lib/puppet/yaml/node/%s.yaml' % argv[1]) as f:
        system_role = yaml.load(f)['facts']['values']['system_role']
        #print system_role['facts']['values']['system_role']
        print yaml.dump({'parameters': {'role': system_role}}, default_flow_style=False)
except BaseException as e:
    raise e

