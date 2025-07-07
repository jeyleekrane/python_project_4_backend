private_message = {"user1": "please check the brench", "user2": "please check the docker", "user3": "please the CI/CD",
                   "user4": "Use Terrform for container orchectration", "user5": "make sure all the service are running on container", }
print(private_message.keys())
print(private_message.values())
print(len(private_message))

for private_messages in private_message:
    print(private_messages, private_message[private_messages])

del private_message["user5"]
print(private_message)
print(len(private_message))


print(len(private_message))
