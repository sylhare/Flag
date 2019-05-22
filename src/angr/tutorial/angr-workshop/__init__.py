'''
docker load -i ./angr-workshop.tar
docker run -d -it --user angr -w /home/angr -v $(pwd):/home/angr/hostcwd -p 8888:8888 angr-workshop:latest jupyter-notebook --ip 0.0.0.0
docker exec -t -u angr 64d0f9244cc9 jupyter notebook list
'''