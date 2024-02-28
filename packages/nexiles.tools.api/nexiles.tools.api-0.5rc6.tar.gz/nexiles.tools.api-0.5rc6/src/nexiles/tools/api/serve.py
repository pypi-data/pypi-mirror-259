from http.server import SimpleHTTPRequestHandler
import socketserver


def serve_directory(PORT):
    if PORT != None:
        try:
            PORT = int(PORT)
            Handler = SimpleHTTPRequestHandler
            httpd = socketserver.TCPServer(("", PORT), Handler)
            print("serving at port", PORT)
            httpd.serve_forever()
        except Exception as e:
            print("Could not start Simple HTTP Server. Error:", e)


def command_serve(api, args):
    serve_directory(args.serve_port)


def add_commands(subparsers, defaults):
    subparser = subparsers.add_parser("serve")

    subparser.add_argument("--port", type=int, default=8080, dest="serve_port")

    subparser.set_defaults(command=command_serve)
