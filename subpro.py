
import os

     #   PORT = 9000

os.system("forever start /home/pi/Taxitv-master/server.js nohup")#This is for no output
os.system("sudo ngrok authtoken 1RNC9uqE9DxrHqtyh90QCigtTru_6bEGQgZQLN4eSj1QZAVKq nohup")#This is for the auth
os.system("sudo ngrok http -subdomain=skywalkerzulu 3000")#This should be the end result

#Handler = http.server.SimpleHTTPRequestHandler


#with socketserver.TCPServer(("", 9000), Handler) as httpd:
    #print("serving at port", 9000)
    #httpd.serve_forever() 

    

   
