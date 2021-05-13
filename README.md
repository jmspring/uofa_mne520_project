# uofa_mne520_project

This repository is for a project for MNE 520 at the University of Arizona, Spring 2021.

The project is a work in progress and is being submitted in it's current state.

The project looks at the use of visualizing [Mineral Resource Data System](https://mrdata.usgs.gov/mrds/) data using
[Open Street Map](https://www.openstreetmap.org) for the mapping layer and [OpenLayers](https://openlayers.org/) as 
the client side interface to interact with the data.

The project leverages this additional functionality:

- [Azure SQL Edge](https://azure.microsoft.com/en-us/products/azure-sql/edge/) for the database
- [Python 3](https://www.python.org/) as the application or backend logic
- [Docker](https://docker.com/) and [Docker Compose](https://docs.docker.com/compose/) to run and manage the application instances
- [Nginx](https://www.nginx.com/) for the web server

The application is quite simple at the moment.  Given a view, the MRDS data is queried to retrieve known site data within the view 
in the browser window.  On the backend, the Python code queries the Azure SQL Edge database to get the features within the current
view.  On the browser side, you can hover over the points and get the name of the site.  If you click on the feature, you will be 
taken to the MRDS public website for that feature.

The current state was expected to be further along, however, a dead keyboard and a switch from Intel architecture to ARM (Intel Mac
to Apple M1 based MacBook Air) complicated the work.

Microsoft SQL Server supports Geo Spatial Queries and other functionality that Azure SQL Edge does not.  Azure SQL Edge is primarily
meant for edge IoT scenarios.  That said, the app reverted to using bounding boxes ans querying the database Lat/Lon data accordingly.

There is a TBD to fully document how to use this example, there is also a TBD to fix the hard coded password.

To use the application, you will need Docker, `docker-compose` and a Unix based shell.  An ARM based computer is not needed, as Azure
SQL Edge supports both Intel and Arm. to run and manage the application instances
- [Nginx](https://www.nginx.com/) for the web server

The application is quite simple at the moment.  Given a view, the MRDS data is queried to retrieve known site data within the view 
in the browser window.  On the backend, the Python code queries the Azure SQL Edge database to get the features within the current
view.  On the browser side, you can hover over the points and get the name of the site.  If you click on the feature, you will be 
taken to the MRDS public website for that feature.

The current state was expected to be further along, however, a dead keyboard and a switch from Intel architecture to ARM (Intel Mac
to Apple M1 based MacBook Air) complicated the work.

Microsoft SQL Server supports Geo Spatial Queries and other functionality that Azure SQL Edge does not.  Azure SQL Edge is primarily
meant for edge IoT scenarios.  That said, the app reverted to using bounding boxes ans querying the database Lat/Lon data accordingly.

There is a TBD to fully document how to use this example, there is also a TBD to fix the hard coded password.

To use the application, you will need Docker, `docker-compose` and a Unix based shell.  An ARM based computer is not needed, as Azure
SQL Edge supports both Intel and ARM.

To run the applicaiton:

- clone the repository
- populate the database
  - from the top level directory, run the script `./scripts/initialize_db.sh "ProspectingGoldForFun!"`
  - again, the password "ProspectingGoldForFun!" is hard coded into the application Python script
- build the application containers by doing `./scripts/build_app.sh "ProspectingGoldForFun!"`
- run the application by doing `./scripts/start_app.sh "ProspectingGoldForFun!"`

When done running the application, you can clean up by executing:

- `./scripts/stop_app.sh`
