import requests




# data to be sent to api 
data = {'client_id':'86suy0ie3evc0n',
        'client_secret': '6AQ2qqCGNtwHxYHH'}


response = requests.post("https://www.linkedin.com/oauth/v2/accessToken", data)
print(response.json)

# AQQC2NVfZVm40bTHQH-xjxajU8urH7BuMIfOb5xs-3rvV1bzb1-LUfXIHnwdSP8QooBxKxJXljclE2Y-AfpukALrdSjyvTLxUiJOpRCOfYuuHQqwEI-leFNtIiUWIQiQKj2DeGbzw9cwL0i0VFvAnLhPjAHjziTfkUpY_0oUN5PsKg7YgE1Ej3vzD7NxDA


https://github.com/indeedlabs/indeed-python
