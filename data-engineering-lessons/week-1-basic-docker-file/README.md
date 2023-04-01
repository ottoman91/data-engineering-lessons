### Basic Docker instructions

* Docker provides containers that are isolated from the rest of the system

* DOCKERFILE contains the settings for creating a new Docker image.

* `docker build -t test:pandas .` is an eg of a command that builds a new Docker
image. The `test:pandas` is the name of the image, and `.` tells Docker to
build the image in the current directory.

* `docker run -it test:pandas` will interactively run a Docker image
