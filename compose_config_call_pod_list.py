######################################################
#  Author:  Bran Wang (branw@vmware.com)
#  Date:    February 12, 2018
#  Func:    use username/password compose config to 
#           k8s API server authorization
######################################################

from kubernetes import client, config


def main():
    config = client.Configuration()

    config.host="https://192.168.112.115:443"
    config.verify_ssl = False

    # use username/password to authorization
    config.username="admin"
    config.password="xxxxx"
    config.api_key['authorization']=config.get_basic_auth_token()

    client.Configuration.set_default(config)

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")

    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()


'''
OUTPUTS:
10.252.3.4      default frontend-696bbbc54-5nw2f
10.252.6.5      default frontend-696bbbc54-kgnkz
10.252.5.6      default frontend-696bbbc54-wm7bh
10.252.3.5      default nginx-deployment-569477d6d8-bnbrh
10.252.6.6      default nginx-deployment-569477d6d8-fpx7l
10.252.5.7      default nginx-deployment-569477d6d8-qp4jt
10.252.6.3      default redis-master-8f949c64d-xkccf
10.252.5.5      default redis-slave-8c758fc8f-blbhs
10.252.6.4      default redis-slave-8c758fc8f-svkph
10.252.5.3      kube-system     heapster-65c44cf7ff-g8svr
192.168.111.16  kube-system     kube-apiserver-k8s-master-0-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.9   kube-system     kube-apiserver-k8s-master-1-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.15  kube-system     kube-apiserver-k8s-master-2-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.16  kube-system     kube-controller-manager-k8s-master-0-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.9   kube-system     kube-controller-manager-k8s-master-1-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.15  kube-system     kube-controller-manager-k8s-master-2-ffea1bd1-da31-4dd3-8f55-7455ee98497f
10.252.3.3      kube-system     kube-dns-cd67f845c-82vmv
10.252.4.2      kube-system     kube-dns-cd67f845c-8ddmk
192.168.111.15  kube-system     kube-flannel-5c82m
192.168.111.13  kube-system     kube-flannel-6mfwc
192.168.111.18  kube-system     kube-flannel-c2ccq
192.168.111.9   kube-system     kube-flannel-cbgnh
192.168.111.16  kube-system     kube-flannel-hnwhg
192.168.111.19  kube-system     kube-flannel-n7svb
192.168.111.16  kube-system     kube-proxy-k8s-master-0-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.9   kube-system     kube-proxy-k8s-master-1-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.15  kube-system     kube-proxy-k8s-master-2-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.19  kube-system     kube-proxy-k8s-node-0-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.13  kube-system     kube-proxy-k8s-node-1-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.5   kube-system     kube-proxy-k8s-node-2-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.16  kube-system     kube-scheduler-k8s-master-0-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.9   kube-system     kube-scheduler-k8s-master-1-ffea1bd1-da31-4dd3-8f55-7455ee98497f
192.168.111.15  kube-system     kube-scheduler-k8s-master-2-ffea1bd1-da31-4dd3-8f55-7455ee98497f
10.252.6.2      kube-system     kubedns-autoscaler-5cdc665f99-j82tf
10.252.1.2      kube-system     kubernetes-dashboard-5f78896cf6-7bwnv
10.252.5.4      kube-system     monitoring-influxdb-54446f8b96-lpqxf
'''
