# Container Technology
## Introduction
There are numerous ways of running programs on a computer. Here are some of them:
1. Word running on a Windows or OSX PC
1. Mysql database running on a Windows, OSX or Linux
1. Java webserver running on Linux or Windows
1. PHP webserver running on Linux or Windows
1. Python programme running on OSX or Linux

All these are examples of programms running on bare metal or as close as you are going to get with the 
operating system between you controlling disks and memory. Lets call this the bare metal world.

## Interpreters
Java and other programs that contain an interpreter to abstract the bare metal further 
and provide an layer between the running program and operating system. Java rather 
confusingly calls its interpreter the Java Virtual Machine. The idea
is to allow the interpreter to be ported to a different operating system so that
the program being run doesn't need to change as long as the interpreter APIs are used. 
This idea has been applied successfully to programmes running Java, PHP, Python etc.. 
However, non of these systems replace the operating system.

## Virtual Machines
An extension of interpreter idea is the virtual machine which in fact replaces the operating system
to allow programs to run inside the virtual machine as if they had a bare metal operating system.
In fact virtual machine technology like Virtual Box or XXX pass through operating system 
calls to the underlying operating system after. In this world a Linux virtual machine can have Windows
as its underlying operating system and each virtual machine is self contained and only interacts 
with the rest of the world through network ports or shared disks. CPU and memory is never shared,
unlike Interpreters.

## Containers
Containers are like virtual machines but much ligher weight. That is they have a much thinner
layer to the underlying operating system and as a consequence the underlying operting system the
container technology runs on must be similar to the container. An example of a container system is 
Docker which allows linux containers to run on Linux only.
However, Docker can still run on Windows or OSX but in these situations it needs a virtual machine
to provice a Linux environment to the container.
In general it does matter which Linux distribution is used as long as is supports Linux containers
also called name spaces.
There are further restrictions to containers as the operting system in the container is kept as
minimal as possible and in practice most people run one programme in a container. So a database
would run in a container and a webserver would run in a separate container and they would 
connect via network ports or more rarely shared disk.

## Comparison




