from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>
            Table
        </title>
    </head>
    <body>
        <h2 align="center">Device Specification(Harish)</h2>
   <table border="5" cellpadding="10" align="center" cellspacing="5">
    <tr bgcolor="sky blue">
    <th>S.No</th>
    <th>Device Specification</th>
    <th>Type</th>
    </tr>
    <tr bgcolor="peachpuff">
    <td>1</td>
    <td>Device Name</td>
    <td>Harish Parthiban-CSE</td>
    </tr>
    <tr bgcolor="peachpuff">
        <td>2</td>
        <td>Processor</td>
        <td>Intel Core Ultra 5 125H</td>
    </tr>
    <tr bgcolor="peachpuff">
        <td>3</td>
        <td>Installed RAM</td>
        <td>16 GB</td>
    </tr>
    <tr bgcolor="peachpuff">
        <td>4</td>
        <td>System Type</td>
        <td>64 bit operating system</td>
    </tr>
    <tr bgcolor="peachpuff">
        <td>5</td>
        <td>Pen and Touch</td>
        <td>No pen and touch available for this device</td>
    </tr>
   </table>
            
        
        
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()