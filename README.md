# Time Zone Converter Application

This is a small app to convert time zones using _python3 flask and vuejs_.You can convert your current time to different time zone with a touch. 
Main features of the application,
   - Get the inserted time zones from the backend and display
   - Display the current time and it's name
   - Display the different time zone's date, time and it's name.

If you like to add more time zones, you just need to add it to the json file which is in convert-time-zone-backend project's timezone.json file.
   ```
   {
       "timeZones": [
           {
               "id": "1",
               "name": "US/Eastern"
           },
           {
               "id": "2",
               "name": "US/Central"
           },
           {
               "id": "3",
               "name": "YOUR TIME ZONE HERE"
           },
       ]
   }
   ```
## Libraries used

Out of many, there are two libraries used to developed this application.

### Pytz
This Python library allows cross platform timezone calculations using Python 2.4 or higher.

ex :-
   ```
   import pytz
   .
   .
   .
   currentDateAndTime = datetime.now(pytz.timezone(selectedTimeZoneName)) #used to get the different time zone value
   ```
 ### Axios
 This a simple promise based HTTP client for the browser and node.js.
 ex :-
   ```
   import axios from 'axios';
   .
   .
   axios.get(constants.url+'/api/getalltimezones')
     .then(res =>{
       let data = res.data;
       this.isLoadedTimeZones = true;
       const results = [];
       for (const i in data.timeZones) {
         results.push({
           id: data.timeZones[i].id,
           name: data.timeZones[i].name,
         });
       }
         this.allTimeZones = results;
     }).catch(error =>{
         console.log(error);
     });
  ```

## Deployement

Python flask app is hosted on the AWS EC2 instance. You can access the live endpoint using following url.
   ```
   awsUrl = 'http://ec2-3-15-4-250.us-east-2.compute.amazonaws.com:8080';
   ```
Frontend with vuejs is in an apache server(cPanel) and assigned a domain name to it.

You can access the live timezoneconverter app using this url : http://timezoneconverter.cf/

Let's have a look, how you can deploy this on your local machine. 

## Convert-Time-Zone-Frontend

Get a clone from this repository and go to convert-time-zone-frontend folder. 
Required: Node.js in your machine.

### Project setup
Install all the node modules to your project. 
```
npm install
```

### Compiles and hot-reloads for development
After succesfully installed all the node modules, can run the project project using following command. 
```
npm run serve
```

### Compiles and minifies for production
If need to deploy the frontend to any other platform, use this command. 
```
npm run build
```
The frontend project will run on : http://localhost:8080

## Convert-Time-Zone-Backend

Get a clone from this repository and go to convert-time-zone-backend folder. 
Required : python3

### Project setup
To install all the libraries which you need, run the following command. 
```
pip3 install -r requirements.txt
```
### Run the project
Following command will run the server.py file. 
```
python server.py
```
The backend project will run on url: http://localhost:3000

## Deployed Application 

Below image shows the time zone converter application which is developed and deployed. 

![This is an image](https://github.com/pasan04/time-zone-conversion/blob/main/ReadMe_Image.PNG)
