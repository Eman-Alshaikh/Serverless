from http.server import BaseHTTPRequestHandler
from urllib import parse 
import platform


class handler(BaseHTTPRequestHandler):
    

    def do_GET(self):
        mypath=self.path 
        url_components=parse.urlsplit(mypath)
        query_string_list=parse.parse_qsl(url_components.query)
        dic=dict(query_string_list)
        name=dic.get("name") 
       
        if name :
            msg=f"i hope for you a nice day {name.upper()}"
        else:
            msg="i hope for you a nice day"

        self.send_response(200)
        self.send_header('Content-typer','text/plain')
        self.end_headers()
        
        self.wfile.write(msg.encode())
         
   