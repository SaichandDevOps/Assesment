# Assesment

Create a script in Python that takes an input from the command line and will connect to JSON Placeholder website (https://jsonplaceholder.typicode.com/) and retrieve sample JSON response from the sub-domain the user entered. Parse the JSON response and place and create a new file and post the parsed contents in the file. Please refer below to what contents needs to be parsed for each endpoint:

/user - name, phone, address
/comments - name, email, body
/album - title
/photos - title, url
/todos - title

File to which the data is posted can be any format (Eg: .txt, .docx,.pdf etc)

Sample Input : user
Sample Output : user.txt file has been created 

Contents of the user.txt file 

List of all Users 

Name - <Name>
Phone - <Phone >
Address -  <address>

.
.
.

EOF

 Input: 
 please enter a sub domain name: users
 Allowed Input Values:
  users
  comments
  album
  photos
  todos
