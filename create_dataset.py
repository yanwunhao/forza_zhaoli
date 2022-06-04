import random
import csv

type_features = [
    [5, 6, 7, 5, 8, 4, 7, 6, 6, 4, 5, 5, 5, 5, 6, 7, 6, 8, 8, 4, 4, 5, 5, 6, 4, 4],
    [8, 6, 4, 6, 5, 5, 4, 5, 7, 7, 4, 5, 5, 6, 5, 5, 5, 4, 5, 5, 5, 5, 6, 5, 5, 7],
    [6, 4, 5, 4, 7, 4, 5, 8, 4, 4, 8, 4, 5, 6, 4, 5, 5, 7, 8, 8, 8, 7, 4, 4, 5, 6],
    [5, 5, 5, 6, 5, 6, 7, 6, 6, 5, 8, 5, 5, 4, 7, 8, 7, 5, 4, 7, 5, 5, 5, 8, 4, 5]
]

interests = ['A', 'B', 'C', 'D', 'E', 'F']

users = []

for user_id in range(476):
    user_type = random.randint(1, 4)
    if user_type == 1:
        # generate user age
        random_seed_for_age = random.random()
        if random_seed_for_age < 0.3:
            user_age = 20
        elif random_seed_for_age > 0.7:
            user_age = 40
        else:
            user_age = 30
        # generate user gender
        random_seed_for_gender = random.random()
        if random_seed_for_gender < 0.3:
            user_gender = 'male'
        else:
            user_gender = 'female'
        # generate season
        user_season = 'winter'
        # generate interests
        user_interests = []
        for interest in interests:
            random_seed = random.random()
            if interest == 'C' or interest == 'D':
                if random_seed < 0.3:
                    continue
                else:
                    user_interests.append(interest)
            else:
                if random_seed < 0.3:
                    user_interests.append(interest)
                else:
                    continue
        # generate user score
        user_score = []
        empty_seed = random.uniform(0.2, 0.6)
        for score in type_features[0]:
            empty_random_seed = random.random()
            shake_seed = random.randint(-2, 2)
            if empty_random_seed < empty_seed:
                user_score.append(None)
            else:
                user_score.append(score + shake_seed)
    elif user_type == 2:
        # generate user age
        random_seed_for_age = random.random()
        if random_seed_for_age < 0.3:
            user_age = 30
        elif random_seed_for_age > 0.7:
            user_age = 50
        else:
            user_age = 40
        # generate user gender
        random_seed_for_gender = random.random()
        if random_seed_for_gender < 0.3:
            user_gender = 'male'
        else:
            user_gender = 'female'
        # generate season
        user_season = 'summer'
        # generate interests
        user_interests = []
        for interest in interests:
            random_seed = random.random()
            if interest == 'A' or interest == 'B':
                if random_seed < 0.3:
                    continue
                else:
                    user_interests.append(interest)
            else:
                if random_seed < 0.3:
                    user_interests.append(interest)
                else:
                    continue
        # generate user score
        user_score = []
        empty_seed = random.uniform(0.2, 0.6)
        for score in type_features[1]:
            empty_random_seed = random.random()
            shake_seed = random.randint(-2, 2)
            if empty_random_seed < empty_seed:
                user_score.append(None)
            else:
                user_score.append(score + shake_seed)
    elif user_type == 3:
        # generate user age
        random_seed_for_age = random.random()
        if random_seed_for_age < 0.3:
            user_age = 10
        elif random_seed_for_age > 0.7:
            user_age = 30
        else:
            user_age = 20
        # generate user gender
        random_seed_for_gender = random.random()
        if random_seed_for_gender < 0.3:
            user_gender = 'female'
        else:
            user_gender = 'male'
        # generate season
        user_season = 'winter'
        # generate interests
        user_interests = []
        for interest in interests:
            random_seed = random.random()
            if interest == 'B' or interest == 'E':
                if random_seed < 0.3:
                    continue
                else:
                    user_interests.append(interest)
            else:
                if random_seed < 0.3:
                    user_interests.append(interest)
                else:
                    continue
        # generate user score
        user_score = []
        empty_seed = random.uniform(0.2, 0.6)
        for score in type_features[2]:
            empty_random_seed = random.random()
            shake_seed = random.randint(-2, 2)
            if empty_random_seed < empty_seed:
                user_score.append(None)
            else:
                user_score.append(score + shake_seed)
    elif user_type == 4:
        # generate user age
        random_seed_for_age = random.random()
        if random_seed_for_age < 0.3:
            user_age = 40
        elif random_seed_for_age > 0.7:
            user_age = 50
        else:
            user_age = 50
        # generate user gender
        random_seed_for_gender = random.random()
        if random_seed_for_gender < 0.3:
            user_gender = 'female'
        else:
            user_gender = 'male'
        # generate season
        user_season = 'spring'
        # generate interests
        user_interests = []
        for interest in interests:
            random_seed = random.random()
            if interest == 'D' or interest == 'F':
                if random_seed < 0.3:
                    continue
                else:
                    user_interests.append(interest)
            else:
                if random_seed < 0.3:
                    user_interests.append(interest)
                else:
                    continue
        # generate user score
        user_score = []
        empty_seed = random.uniform(0.2, 0.6)
        for score in type_features[3]:
            empty_random_seed = random.random()
            shake_seed = random.randint(-2, 2)
            if empty_random_seed < empty_seed:
                user_score.append(None)
            else:
                user_score.append(score + shake_seed)
    users.append([user_id, user_age, user_gender, user_season, user_interests, user_score])

with open('./new_dataset_zhaoli.csv', 'w') as f:
    csvWriter = csv.writer(f)
    for user in users:
        csvWriter.writerow(user)
    f.close()

