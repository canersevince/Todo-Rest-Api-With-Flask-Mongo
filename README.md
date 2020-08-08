# Example todo rest api with Flask & MongoDB
App currently has 2 endpoints.

You can test it with postman/insomnia etc.
deployed on : 
https://csfluttertodo.herokuapp.com/


# endpoints : 
_/create_user
expected data = 
user : {name: "...", email: "...", password: "...", todo : []}
 
_/add_todo
expected data = 
user: { name : "...", email: "..@..com", todos : [... updated todos] }

