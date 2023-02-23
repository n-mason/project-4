# UOCIS322 - Project 4 #

## Name: Nathaniel Mason

## Contact Info: nmason@uoregon.edu

## Project Description:
The goal of this project is to create a web application based on RUSA's online calculator for a brevet
*The application is a site found on the web that allows the user to choose a distance and start date, then after
entering the distance value of a brevet controle, the opening and closing time of the controle will be displayed
*The algorithm is based on the algorithm from the RUSA website, which can be found at: [https://rusa.org/pages/acp-brevet-control-times-calculator]

### To start the application, the user should use the following docker commands:
*"docker build -t myimage ." to build your image (you can also use docker images to list existing images and check that the creation was successful)
*"docker run -d -p 5001:5000 myimage" to create a running container and set the port that you will access on your browser (you can also use docker ps to view existing containers and check that your container is created and running)
#### Now that the docker container is created and running, you can access the application by going to your browser and entering localhost:5001 (5001 is the port you will use from the browser that was defined using the -p tag in docker run)

