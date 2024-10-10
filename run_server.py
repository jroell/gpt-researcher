import uvicorn
from dotenv import load_dotenv
from backend.server import app
import sys
import socket

def find_free_port(start_port=8000, max_port=9000):
    for port in range(start_port, max_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('', port))
                return port
            except OSError:
                continue
    raise IOError("No free ports")

def run_server(port=None):
    load_dotenv()
    if port is None:
        port = find_free_port()

    print(f"Starting FastAPI server on port {port}...")

    # Get the read_root function from the app's routes
    read_root = next(route for route in app.routes if route.path == "/").endpoint

    # Wrap the read_root function with a breakpoint
    def debug_read_root(*args, **kwargs):
        print("Hitting breakpoint in read_root")
        breakpoint()
        return read_root(*args, **kwargs)

    # Replace the original read_root function with our debug version
    for route in app.routes:
        if route.path == "/":
            route.endpoint = debug_read_root
            break

    try:
        uvicorn.run("backend.server:app", host="0.0.0.0", port=port, reload=True)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using a random free port.")
            port = None
    else:
        port = None

    run_server(port)
