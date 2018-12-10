import requests


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return 'https://vk.com/id' + self.user_id

    def friends(self):
        params = {
            'user_id': self.user_id,
            'access_token': 'b8f4df59b8f4df59b8f4df591fb893851fbb8f4b8f4df59e4f32e1ada56fd16a8dcd160',
            'v': '5.92',
            'fields': 'domain'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        friends_data = response.json()
        friends_set = set()
        for friend in friends_data['response']['items']:
            friends_set.add(friend['id'])
        return friends_set

    def __and__(self, other):
        compared_friends = list(self.friends() & other.friends())
        user_list = [User(i) for i in compared_friends]
        print(user_list)


if __name__ == "__main__":
    user1 = User('4133803')
    user2 = User('4329052')
    user1 & user2
    print(user1)
    print(user2)

