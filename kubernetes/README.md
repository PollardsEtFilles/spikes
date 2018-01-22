
## How to Install Docker with Kubernetes on a Mac
### Prerequisites
* If you have installed kubectl before make sure its uninstalled before you install.
* If you have installed minikube before make sure its uninstalled before you install.

### Warnings
* Installing Edge will delete all your images and containers.
* Do not try to install minikube as it uses an old version of Docker that is incompatible
with Docker For Mac

### Install Docker with Kubernetes 
Download the Edge version from here
https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac
and follow the instructions here https://docs.docker.com/docker-for-mac/#kubernetes to enable 
and start Kubernetes as its not enabled by default (you can leave the other default options as is).

After installing Docker and enabling Kubernetes makes sure its configuration is pointing to 
docker-for-mac as follows:

    kubectl config get-contexts
    kubectl config use-context docker-for-desktop

### Run the Kubernetes UI
Setup the UI, once only (see https://github.com/kubernetes/dashboard)

    kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml

Run the UI, every time you need it. Note. This process doesn't run in the background and ctr-c stops it

    kubectl proxy

And in a web browser http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#!/overview?namespace=default
    
    
## Build a container and test it works with Docker and Kubernetes
Go to ../docker/pypiserver

    ./build.sh
    # check the pypi image exists
    docker images

    # run it interactively with Docker - 
    docker run -it --rm -p 8080:80 pef/pypi:1.0.0

    # check its running and test in separate terminal
    docker ps
    curl http://localhost:8080
    # stop the container with ctrl-c

    # start pypi on kubernetes, check its running and test connectivity
    kubectl run --image=pef/pypi:1.0.0 pypi --image-pull-policy=IfNotPresent 
    kubectl get pods
    # use the full name of pypi, for example
    
    kubectl get pods
    NAME                   READY     STATUS    RESTARTS   AGE
    pypi-df7b67c87-wlz8b   1/1       Running   0          1m
    
    kubectl port-forward pypi-df7b67c87-wlz8b 8080:80
    
    curl http://localhost:8080
    
    # delete the server from Kubernetes
    kubectl delete deployment pypi

## Run services in a docker-compose.yml

    docker stack deploy --compose-file docker-compose.yml pypi-db
    # and delete it
    docker stack rm pypi-db
    
## References
1. https://kubernetes.io/docs/reference/kubectl/docker-cli-to-kubectl/
1. https://docs.docker.com/docker-for-mac/kubernetes/
1. https://rominirani.com/tutorial-getting-started-with-kubernetes-with-docker-on-mac-7f58467203fd
1. https://docs.docker.com/registry/configuration/
1. https://kubernetes.io/docs/reference/kubectl/cheatsheet/
1. https://github.com/kubernetes/dashboard