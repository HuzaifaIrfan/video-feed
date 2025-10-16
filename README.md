<div align="center">
  <h1>Video Feed Deployment</h1>
  <p><h3 align="center">Video Feed (app/crawler) Docker/Kubernetes Deployment Repo 🚀</h3></p>
</div>

https://github.com/HuzaifaIrfan-Web/video-feed-app
•
https://github.com/HuzaifaIrfan-Web/video-feed-crawler

<hr>

# 🚀 Usage
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


# 📝 Documentation

# 📚 References


# 🤝🏻 Connect with Me

[![GitHub](https://img.shields.io/badge/Github-%23222.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HuzaifaIrfan/)
[![Website](https://img.shields.io/badge/Website-%23222.svg?style=for-the-badge&logo=google-chrome&logoColor==%234285F4)](https://www.huzaifairfan.com)

# 📜 License

Licensed under the GPL3 License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)

Last Updated on 2025-04-28
