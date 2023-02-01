# BioPath
More detailed documentation for each componenet found in the README at...
* [Backend](https://github.com/SD-2022-CPSC-10/BioPath/tree/api/backend#biopath-backend)
* [Frontend](https://github.com/SD-2022-CPSC-10/BioPath/tree/api/frontend)

### GU BioPath web app

To run:
Install Docker Desktop
From the directory containing docker-compose.yaml: ```$ docker-compose build```

This will build the docker containers (it might take a while the first time)

Then to start the applications: ```$ docker-compose up -d```

The -d stands for detached mode

To check he status of your Docker containers either
1. Look at Docker Desktop
2. run ```$ docker-compose ps -a```

To stop the app: ```$ docker-compose down```



### Filesystem
```
BioPath
│   README.md
│   docker-compose.yaml 
│
└───frontend
│   │   Dockerfile
│   │   package.json
|   |   package-lock.json
│   │
│   └───public
|   |   |   $ Any assets the front end might need
│   |   │   manifest.json $ Manifest of assets
|   └───src
|       |   App.js $ Core React component
|       |   App.css
|       |   index.js
|       |   index.css
|       |   logo.svg
|       |   reportWebVitals.js
|       └───views
|       |   |   $ Upper level page views
|       |   |   PathwayView.js
|       |   |   PathwayView.css
|       └───components
|       |   |   $ React components in js/css pairs
|       |   |   Component.js
|       |   |   Component.css
│   
└───backend: details in backend directories README
|   |   ...
```

