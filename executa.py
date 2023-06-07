import threading

# Function to execute the generated Python code in a new thread
def executa(code):
    def target():
        exec(code)
    thread = threading.Thread(target=target)
    thread.start()