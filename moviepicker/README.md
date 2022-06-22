[Docker Tutorial For Beginners - How To Containerize Python Applications](www.youtube.com/watch?v=bi0cKgmRuiA&)

prerequisites
-Visual Studio Code (mac)
-docker desktop (mac)

Open Visual Studio Code and connect to github and clone PYTHON-FUN repository locally
type: cd moviepicker in the terminal to change to the local folder within the local repository "moviepicker"
type: docker build -t python-imdb .
type: docker run -t -i python-imdb

The python program will execute in the container, connect to the internet and query IMDB and return with a random movie.
Next you will answer Y/N to the question: Do you want another movie (y/[n]?
Type n to end the program and close the container

type: docker run -t -i python-imdb to execute the python program again!
