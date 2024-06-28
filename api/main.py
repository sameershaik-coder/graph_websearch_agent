from agent_graph.graph import create_graph, compile_workflow

# server = 'ollama'
# model = 'llama3:instruct'
# model_endpoint = None



# server = 'vllm'
# model = 'meta-llama/Meta-Llama-3-70B-Instruct' # full HF path
# model_endpoint = 'https://kcpqoqtjz0ufjw-8000.proxy.runpod.net/' 
# #model_endpoint = runpod_endpoint + 'v1/chat/completions'
# stop = "<|end_of_text|>"



from fastapi import FastAPI
from api.routers import search
from utils import file
app = FastAPI()

app.include_router(search.router)

@app.get("/{query}")
def read_root(query: str):
    server = 'openai'
    model = 'gpt-3.5-turbo'
    model_endpoint = None
    iterations = 40

    print ("Creating graph and compiling workflow...")
    graph = create_graph(server=server, model=model, model_endpoint=model_endpoint)
    workflow = compile_workflow(graph)
    print ("Graph and workflow created.")

    verbose = False

    dict_inputs = {"research_question": query}
    # thread = {"configurable": {"thread_id": "4"}}
    limit = {"recursion_limit": iterations}

    for event in workflow.stream(
        dict_inputs, limit
        ):
        if verbose:
            print("\nState Dictionary:", event)
        else:
            print("\n")
    
    response = file.read_json_file()    
    return response