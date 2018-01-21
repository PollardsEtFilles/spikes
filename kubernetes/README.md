
## How to Install Docker with Kubernetes on a Mac
Download the Edge version from here
https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac
and follow the instructions here to enable and start Kubernetes (you can leave the other default 
options as is)
https://docs.docker.com/docker-for-mac/#kubernetes

Note:
* Installing Edge will delete all your images and containers.
* If you have installed kubectl before make sure its uninstalled.

After installing Docker and enabling Kubernetes makes sure its configuration is pointing to 
docker-for-mac as follows:

    kubectl config get-contexts
    kubectl config use-context docker-for-desktop

### Run the Kubernetes UI
Setup the UI, once only

    kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml

Run the UI, every time you need it. Note. This process doesn't run in the background and ctr-c stops it

    kubectl proxy

## Build a container and test it works with Docker and Kubernetes
Go to ../docker/pypiserver

    ./build.sh
    # check the pypi image exists
    docker images

    # run it interactively with Docker - 
    docker run -it --rm -p 80:8080 pef/pypi:1.0.0

    # check its running and test in separate terminal
    docker ps
    curl http://localhost:8080
    # stop the container with ctrl-c

    # start pypi on kubernetes, check its running and test connectivity
    kubectl run --image=pef/pypi:1.0.0 pypi --port=808 --image-pull-policy=IfNotPresent 
    kubectl get pods
    kubectl port-forward pypi 8080:80
    
    curl http://localhost:8080
    
    # delete the server from Kubernetes
    kubectl delete deployment pypi

## References
1. https://kubernetes.io/docs/reference/kubectl/docker-cli-to-kubectl/
1. https://docs.docker.com/docker-for-mac/kubernetes/
1. https://rominirani.com/tutorial-getting-started-with-kubernetes-with-docker-on-mac-7f58467203fd
1. https://docs.docker.com/registry/configuration/
1. https://kubernetes.io/docs/reference/kubectl/cheatsheet/