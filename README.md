# Sound Stream Controller

Application that allows to control sounds and music for a Stream, using VLC and StreamLabs Desktop.

This application runs a FastAPI python application, and a front end made with React.

The Backend allow to play, stop, next or prev song; and get all the songs from a directory.

The Front end allow to call the api using a webpage.

## Install and configure applications

To Run the application, you need to install and configure the dependencies from each application:

### Backend

To Run the Backend, you will need Python 3.10 or later, and install Pipenv using ```pip```:

```bash
pip install pipenv
```

You need to create an ```.env``` file with the following Environment Variables:

* ```SONG_DIR```: Songs Directory Path.
* ```STREAM_PATH```: Folder path where the file ```cursong.txt``` will be created.

Later, run the application using the current Pipfile, from ```back``` folder:

```bash
cd back
pipenv run fastapi dev backend.py
```

This will create an virtual environment, and install al the dependencies (like fastapi and python_vlc); later, the fastapi development server is launch; and the application is located at ```http://localhost:8000```.

### FrontEnd

To Run the Frontend, you will need to install NodeJS, and NPM.

First; install all the dependencies, from the ```packages.json``` file at the ```front``` folder:

```bash
cd front
npm install
```

This will install al the dependencies for the application; later you can start the application using:

```bash
npm run start
```

This will start the development server for the React Application; you can locate this application at the address ```http://localhost:3000```.
