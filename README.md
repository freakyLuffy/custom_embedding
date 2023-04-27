# custom_embedding

## API for OpenAI Trained Data
This is an API built on Flask that interacts with OpenAI's GPT-3 language model. The purpose of this API is to receive queries related to the trained data and return the appropriate responses.

Train the data by creating a docs folder in the same directory as app.py. Put the data you want to train in a PDF format inside the docs folder. Then run model_generator.py to generate the trained model.

Install the required packages using ```pip install -r requirements.txt```
Set up your OpenAI API credentials by following the instructions in the OpenAI API documentation.
Run the API by executing python app.py in the command line.


## Usage

Endpoints
The API has one endpoint:

POST /chatbot
Request
The request body must contain a JSON object with the following keys:

query (string): The query related to the trained data.
Example request body:

```
{
   "input_text": "how many items do you have",
    "filename": "index.json",
    "key": "your_open_api_key",
    "format": "json"
}
```
Please note that you should replace "your_open_api_key" with your actual OpenAI API key. Additionally, the filename parameter may vary depending on the format of your data.

Response
The API will respond with a JSON object containing the following keys:

response (string): The response to the query based on the trained data.

Example response body:

```
{
  "response": "I have 5 items."
}
```
Notes
The API currently uses the davinci engine of GPT-3. You can change this by modifying the ENGINE constant in app.py.
The API uses the openai package to interact with the OpenAI API. You can find more information on this package in the OpenAI API documentation.
This API is intended for use with trained data. It is not designed to handle arbitrary queries.



