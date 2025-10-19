# Internship-Assignment
Testing Python Code with Flask API Framework and Ollama <br> <br>

## Install Dependencies
- Download Ollama ( Model : llama3 ) <br> <br>
Framework Required : <br> <br>
`pip install flask` <br> <br>
`pip install Ollama` <br> <br>
 
## Run Flask App
### Step by Step ( Command Prompt / curl ) : <br>
1. python app.py to run flask app <br>
2. `curl -X POST -H "Content-Type: application/json" -d "{\"prompt\": \"What do you think about coding?\"}" http://127.0.0.1:5000/inference` <br>
note : inside of prompt could be any prompt <br>
3. Check API Status code command prompt ( if status code is 200 that means the code works )<br> <br>

### Step by Step ( POSTMAN ) : <br>
1. Open POSTMAN <br>
2. go to collection and use POST Method <br>
3. type endpoint ( example : http://127.0.0.1:5000/inference ) <br>
4. press body and type <br>
{ <br>
	"prompt": "What do you think about coding?" <br>
} <br>
5. below you can see the response in JSON format <br>
6. Check API Status code command prompt ( if status code is 200 that means the code works )<br>
