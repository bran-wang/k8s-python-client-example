#!/usr/bin/env python
# encoding: utf-8

import os
from kubernetes import client, config

config.load_kube_config(
    os.path.join(os.environ["HOME"], '.kube/config')
)

v1 = client.CoreV1Api()

pod_list = v1.list_namespaced_pod("default")
for pod in pod_list.items:
    print("%s\t%s\t%s" % (pod.metadata.name, pod.status.phase, pod.status.pod_ip))




'''
OUTPUTS:
frontend-696bbbc54-5nw2f        Running 10.252.3.4
frontend-696bbbc54-kgnkz        Running 10.252.6.5
frontend-696bbbc54-wm7bh        Running 10.252.5.6
redis-master-8f949c64d-xkccf    Running 10.252.6.3
redis-slave-8c758fc8f-blbhs     Running 10.252.5.5
redis-slave-8c758fc8f-svkph     Running 10.252.6.4
'''
