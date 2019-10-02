
import os

     #   PORT = 9000

os.system("forever start server.js nohup")
os.system(" authtoken 1RNC9uqE9DxrHqtyh90QCigtTru_6bEGQgZQLN4eSj1QZAVKq")
os.system(" ngrok http -subdomain=skywalkerzulu 3000")

#Handler = http.server.SimpleHTTPRequestHandler


#with socketserver.TCPServer(("", 9000), Handler) as httpd:
    #print("serving at port", 9000)
    #httpd.serve_forever() 

    

   
