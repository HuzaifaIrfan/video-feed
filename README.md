# video-feed

## Create namespace

```sh
kubectl apply -f namespace.yml
```

## Create GHCR PAT

```sh
kubectl create secret docker-registry ghcr-secret --namespace=video-feed --docker-server=ghcr.io --docker-username=huzaifairfan --docker-password="ghp_xxxx"
```

### See Secret
```sh
kubectl get secrets -n video-feed
```

## Deployment

```sh
kubectl apply -f video-feed-deployment.yml
```

```sh
kubectl apply -f video-feed-ingressroute.yml
```

## See Deployment

```sh
kubectl get all -n video-feed
```

## Delete Deployment

```sh
kubectl delete -f video-feed-deployment.yml 
```

