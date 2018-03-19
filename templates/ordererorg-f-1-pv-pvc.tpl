apiVersion: v1
kind: PersistentVolume
metadata:
  name: {{clusterName}}-ordererorg-f-1-pv
spec:
  capacity:
    storage: 500Mi
  accessModes:
    - ReadWriteMany
  nfs:
    path: /opt/share/{{clusterName}}/resources/crypto-config/ordererOrganizations/ordererorg-f-1
    server: 10.160.40.95  #change to your nfs server ip here

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 namespace: {{clusterName}}
 name: {{clusterName}}-ordererorg-f-1-pv
spec:
 accessModes:
   - ReadWriteMany
 resources:
   requests:
     storage: 10Mi

---
