print "Cristian's Algorithm"
client = 100
server = 200 
print "Client sends request to Server for time synchronization"
print "Current Client TIme : ",client
print "Current Server Time : ",server
print "Please enter the server processing time in the following format : HH:MM:SS"
server_time = int(raw_input())
Tnew        = server_time + ((server - client)/2)
client_new  = client + Tnew 
print "New client time :",client_new


