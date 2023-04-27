from flask import Flask, request, jsonify,make_response
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os

app = Flask(__name__)
def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    my_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(my_dir, 'index.json')
    index.save_to_disk(json_file_path)

    return index

def chatbot(input_text,filename='index.json'):
    my_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(my_dir, filename)
    index = GPTSimpleVectorIndex.load_from_disk(json_file_path)
    response = index.query(input_text, response_mode="compact")
    return response.response



@app.route('/chatbot', methods=['POST'])
def handle_chatbot():
    input_text = request.json['input_text']
    try:
        filename = request.json['filename']
    except KeyError:
        filename = None
    key=request.json['key']
    os.environ["OPENAI_API_KEY"] = key
    if filename:
        response = chatbot(input_text,filename)
    else:
        response=chatbot(input_text)

    if request.json['format'] == 'html':
        # Send an HTML response
        html = response
        return make_response(html, 200, {'Content-Type': 'text/html'})
    else:
        # Send a JSON response
        return jsonify({'response': response})

@app.route('/', methods=['GET'])
def handle():
    return "okay"

if __name__ == '__main__':
    app.run(debug=True)
