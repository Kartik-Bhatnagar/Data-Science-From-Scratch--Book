users =[
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#initilize the friendship dictionary with the key as user id and list as friends

friendships = {user["id"]:[] for user in users}
print(friendships)
print("And loop over the friendship pairs to populate it:")

for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
    
print(friendships)    
def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)
total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)


# Create a list (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(num_friends_by_id)

num_friends_by_id.sort( # Sort the list
    key=lambda id_and_friends: id_and_friends[1], # by num_friends    
    reverse=True) # largest to smallest
    
print(num_friends_by_id)    