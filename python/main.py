def main():
    info = [
        {'name': 'Andrew D. Huberman', 'age': 48},
        {'name': 'Marco Rubio', 'age': 52},
        {'name': 'Lindsey Graham', 'age': 68},
        {'name': 'Ted Cruz', 'age': 52},
        {'name': 'Brian Tracy', 'age': 79},
        {'name': 'Jim Rohn', 'age': 79},
        {'name': 'Donald Trump', 'age': 77},
        {'name': 'Russell Westbrook', 'age': 34},
        {'name': "Luka Dončić", 'age': 25},
        {'name': 'LeBron James', 'age': 38},
        {'name': 'Chris Paul', 'age': 38},
        {'name': 'Kevin Durant', 'age': 34},
        {'name': 'Jayson Tatum', 'age': 25},
        {'name': 'P. J. Tucker', 'age': 38},
        {'name': "De'Anthony Melton", 'age': 25},
        {'name': "Jalen McDaniels", 'age': 25},
    ]
    results = dict()
    for i in info:
        if i.get('age') not in results:
            results[i.get('age')] = []
        results[i.get('age')].append(i.get('name'))
    print("Welcome", results)


if __name__ == '__main__':
    main()
