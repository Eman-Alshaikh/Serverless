from http.server import BaseHTTPRequestHandler
from urllib import parse 
import platform


class handler(BaseHTTPRequestHandler):
    

    def do_GET(self):
        path=self.path 
        url_components=parse.urlsplit(path)
        query_string_list=parse.parse_qsl(url_components.query)
        dic=dict(query_string_list)
        name=dic["name"].upper()
        my_name=f"{name},{name}!"

        self.send_response(200)
        self.send_header('Content-typer','text/plain')
        self.end_headers()
        
        self.wfile.write((my_name).encode())
        return
      