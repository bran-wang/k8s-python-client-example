#!/usr/bin/env python
# encoding: utf-8

import os
import yaml

from kubernetes import client, config


def create_deployment(namespace, data, **kwargs):
    try:
        k8s_client = client.ExtensionsV1beta1Api()
        resp = k8s_client.create_namespaced_deployment(namespace, data, **kwargs)
        print resp
    except client.rest.ApiException as e:
        print e
    except Exception as e:
        print e


def create_service(namespace, data, **kwargs):
    try:
        k8s_client = client.CoreV1Api()
        resp = k8s_client.create_namespaced_service(namespace, data, **kwargs)
        print resp
    except client.rest.ApiException as e:
        print e
    except Exception as e:
        print e


def create_persistent_volume_claim(namespace, data, **kwargs):
    try:
        k8s_client = client.CoreV1Api()
        resp = k8s_client.create_namespaced_persistent_volume_claim(namespace, data, **kwargs)
        print resp
    except client.rest.ApiException as e:
        print e
    except Exception as e:
        print e


def create_persistent_volume(data, **kwargs):
    try:
        k8s_client = client.CoreV1Api()
        resp = k8s_client.create_persistent_volume(data, **kwargs)
        print resp
    except client.rest.ApiException as e:
        print e
    except Exception as e:
        print e


def create_namespace(data, **kwargs):
    try:
        k8s_client = client.CoreV1Api()
        resp = k8s_client.create_namespace(data, **kwargs)
        print resp
    except client.rest.ApiException as e:
        print e
    except Exception as e:
        print e


def create_k8s_resource(file_data):
    for data in file_data:
        if data is None:
            continue
        kind = data.get('kind', None)
        name = data.get('metadata').get('name', None)
        namespace = data.get('metadata').get('namespace', None)

        print "namespace={}, name={}, kind={}".format(namespace, name, kind)

        if kind in support_namespace:
            func_dict.get(kind)(namespace, data)
        else:
            func_dict.get(kind)(data)


def deploy_k8s_resource(dir):
    for root, dirs, files in os.walk(dir):
        file_list = [os.path.join(root, f) for f in files if not f.startswith('.')]

        for yaml_file in file_list:
            with open(yaml_file) as f:
                file_data = yaml.load_all(f)
                create_k8s_resource(file_data)


func_dict = {
    "Deployment": create_deployment,
    "Service": create_service,
    "PersistentVolume": create_persistent_volume,
    "PersistentVolumeClaim": create_persistent_volume_claim,
    "Namespace": create_namespace
}


support_namespace = ['Deployment', 'Service', 'PersistentVolumeClaim']


def main():

    config.load_kube_config("kubeconfig.json")

    baas_dir = ["baas/setupCluster/deployment/namespace",
           "baas/setupCluster/deployment/peerOrganizations",
           "baas/setupCluster/deployment/ordererOrganizations"]
    for d in baas_dir:
      deploy_k8s_resource(d)


if __name__ == '__main__':
    main()
