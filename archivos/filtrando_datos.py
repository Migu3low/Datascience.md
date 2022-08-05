from functools import reduce

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # With Comprehensions:
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    # all_mayors = [worker["name"] for worker in DATA if worker ["age"] > 18]
    all_mayors1 = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]

    # With high order functions:

    all_python_devs = list(filter(lambda x: x["language"] == "python" , DATA))
    # print(all_python_devs)
    all_python_devs = list(map(lambda x: x["name"], all_python_devs))
 
    all_Platzi_workers = list(filter(lambda x: x["organization"] == "Platzi", DATA))
    # print(all_Platzi_workers)
    all_Platzi_workers = list(map(lambda x: x["name"], all_Platzi_workers))

    all_mayors = list(filter(lambda x: x["age"] >= 18, DATA))
    all_mayors = list(map(lambda x: x["name"], all_mayors))

    for worker in all_Platzi_workers:
         print(worker) 
            
    for worker in all_mayors:
         print(worker)

    for worker in all_python_devs:
          print(worker)

if __name__ == '__main__':
    run()
