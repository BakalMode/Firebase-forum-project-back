# Instructions

all you need to do in order to make your back end and front end
work together is setting this: CORS(app, origins='http://localhost:3002')
instead of 3002 check on which port you are running the pront end and set in as the port: 'http://localhost:XXXX'                                  


create a virtual environment:                                 
pip install virtualenv(once per computer)                             
python -m virtualenv myenv(once per project)                       
windows:                                                     
myenv\Scripts\activate
macOS:                                                                 
source myenv\bin\activate


run this command in order to install all needed packages on to your  venv: 
pip install -r requirements.txt


after that all you have to do is run the app:                    
for windows:                                                        
Py app.py runserver                                                
for mac:                                                            
python3 app.py runserver



