from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] ='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'
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

index=construct_index("docs")
