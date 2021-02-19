# internet-technology-proj1
## Names and NetIDs
Jeffrey Samson (jas1055)
Aum Pathak (aap273)

## 1. Briefly discuss how you implemented your iterative client functionality.
For a iterative approach, the client approaches the root server with the domain query. If the root server doesn't have the hostname for the top level server then it responds to the client with ns. The hostname returned by the root server is used by the client to connect to the top level server. Once connected it uses the same domain name to reach root server. If the top loevel server has the domain name the client has it return the domain name, IP Address and the flag "a". If these details aren't present then the top level server sends a message saying Hostname - Error:HOST NOT FOUND.

### Implementation
We first use a for loop to iterate over each line in PROJI-HNS.txt and send each line to the root server. The server responds with the domain name, IP, and flag. We then check to see if the flag "A" is present. If it is, we write the message received from the root server in a resolve.txt file. If the "A" flag isn't present we open a connection with the top-level server and send the message from the root server to the top-level server. Then the top level server performs a lookup in the rs-dns table. If the host name is present, the top-level server sends back the host name along with the IP address and the flag. If the host name is not found we send an error message. 
## 2. Are there known issues or functions that aren't working currently in your attached code? If so, explain.
There are no issues, all the code works as expected.
## 3. What problems did you face developing code for this project?
We had an issue in implementing a way to send a message with the DNS Names to the root server before the client side socket closes and using queries to process it on the root server side. 
## 4. Reflect on what you learned by working on this project. 
We learned how to set up connections between the client and server while also dealing with multiple servers. Additionally we learned how to send and recieve messages and data between the client and server. 
