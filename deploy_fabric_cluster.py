#!/usr/bin/env python
# encoding: utf-8

from os import path
import yaml

from kubernetes import client, config


def create_deployment(file, namespace):
    k8s_client = client.ExtensionsV1beta1Api()
    with open(path.join(path.dirname(__file__), file)) as f:
        file_data = yaml.load(f)
        resp = k8s_client.create_namespaced_deployment(body=file_data, namespace=namespace)
    print("Deployment %s created. status='%s'" % str(resp.metadata.name), str(resp.status))

def create_service(file, namespace):
    k8s_client = client.CoreV1Api()
    with open(path.join(path.dirname(__file__), file)) as f:
        file_data = yaml.load(f)
        resp = k8s_client.create_namespaced_service(body=file_data, namespace=namespace)
    print("Service %s created. status='%s'" % str(resp.metadata.name), str(resp.status))

def create_pod(file, namespace):
    k8s_client = client.CoreV1Api()
    with open(path.join(path.dirname(__file__), file)) as f:
        file_data = yaml.load(f)
        resp = k8s_client.create_namespaced_pod(body=file_data, namespace=namespace)
    print("Pod %s created. status='%s'" % str(resp.metadata.name), str(resp.status))


def main():

    config.load_kube_config()

    # Create Deployment
    create_deployment("ca.yaml", "default")
    create_deployment("cli.yaml", "default")
    create_deployment("orderer.yaml", "default")
    create_deployment("peer0.yaml", "default")
    create_deployment("peer1.yaml", "default")
    create_deployment("peer2.yaml", "default")
    create_deployment("peer3.yaml", "default")
    create_deployment("peer-base.yaml", "default")

    # Create Service
    create_service("ca_service.yaml", "default")
    create_service("orderer_service.yaml", "default")
    create_service("peer0.yaml", "default")
    create_service("peer1.yaml", "default")
    create_service("peer2.yaml", "default")
    create_service("peer3.yaml", "default")

    # Create Pod
    create_pod("peer-pod.yaml", "default")


if __name__ == '__main__':
    main()
