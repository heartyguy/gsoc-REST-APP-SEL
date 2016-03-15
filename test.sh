curl -X GET http://localhost:5000/members
# after initiation, one member is in the database
#[{"name": "Tian", "phone": "6471891111"}]
curl -X GET http://localhost:5000/members/Tian
# Get will return a json containing the member info
#{"name": "Tian", "phone": "6471891111", "success": "true"}
curl -X GET http://localhost:5000/members/David
# Get on member 'David' will give error 
#{"error": "Member not in database", "success": "false"}
curl -X PUT -H "Content-Type: application/json" -d '{"name":"David", "phone":"5197483434"}' http://localhost:5000/members/add
#David is added by PUT
#{"David": "5197483434", "success": "true"}
curl -X POST -H "Content-Type: application/json" -d '{"name":"Matt", "phone":"4167483434"}' http://localhost:5000/members/add
#Matt is added by POST
#{"Matt": "4167483434", "success": "true"}
curl -X GET http://localhost:5000/members
#Now the database contains  Tian, David, and Matt
#[{"name": "Tian", "phone": "6471891111"}, {"name": "David", "phone": "5197483434"}, {"name": "Matt", "phone": "4167483434"}]
