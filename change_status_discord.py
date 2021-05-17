import requests, time

token = ""
u_header = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

array = ["HI","HEllo"] # put stuff in the format  ["Thing", "other thing", "other other thing"]
num = 0
while True:
    time.sleep(5) # Prevents rate limiting
    status = array[num]
    requests.patch('https://discord.com/api/v8/users/@me/settings', headers=u_header, json={"custom_status":{"text":status,"expires_at":"2021-04-14T23:00:00.000Z"}}) # Change to current date
    num += 1
    if num == len(array):
        num = 0

