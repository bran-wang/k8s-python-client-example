#!/usr/bin/env python
# encoding: utf-8

from kubernetes import client, config
import time
 
def prn_obj(obj):
    print '\n'.join(['%s:%s' % item for item in obj.__dict__.items()])
 
def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config("/home/vmware/Cello/Test/kubeconfig.json")
    mConfig = client.Configuration()
    prn_obj(config)
    print "---Break---"
    prn_obj(mConfig)
 
 
    time.sleep(1000)
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
 
 
if __name__ == '__main__':
    main()
