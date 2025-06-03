<br />

<div align="center">
  <h1>Video Feed Deployment</h1>
  <p><h3 align="center">Video Feed (app/crawler) Docker/Kubernetes Deployment Repo 🚀</h3></p>
</div>

https://github.com/HuzaifaIrfan/video-feed-app
•
https://github.com/HuzaifaIrfan/video-feed-crawler

<hr>

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


## 🤝🏻 &nbsp;Connect with Me

<p align="center">
<a href="https://www.huzaifairfan.com"><img src="https://img.shields.io/badge/-huzaifairfan.com-1aa260?style=flat&logo=Google-Chrome&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/huzaifairfan/"><img src="https://img.shields.io/badge/-Huzaifa%20Irfan-0072b1?style=flat&logo=Linkedin&logoColor=white"/></a>
<a href="https://github.com/HuzaifaIrfan/"><img src="https://img.shields.io/badge/-Huzaifa%20Irfan-4078c0?style=flat&logo=Github&logoColor=white"/></a>
<a href="mailto:contact@huzaifairfan.com"><img src="https://img.shields.io/badge/-contact@huzaifairfan.com-c71610?style=flat&logo=Gmail&logoColor=white"/></a>
<a href="https://www.instagram.com/huzaifairfan2001/"><img src="https://img.shields.io/badge/-@huzaifairfan2001-cd486b?style=flat&logo=Instagram&logoColor=white"/></a>
<a href="https://www.facebook.com/huzaifairfan2001/"><img src="https://img.shields.io/badge/-@huzaifairfan2001-4267B2?style=flat&logo=Facebook&logoColor=white"/></a>
</p>

## License

Licensed under the MIT License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)