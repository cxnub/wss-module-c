import os, random, string

problem_titles = ['kahns-algorithm', 'convex-hull', 'postfix-expression-evaluation', 'computational-geometry', 'pre-calculation', 'modified-dijkstra', 'tarjans-algorithm', 'add-two-numbers', 'subtract-two-numbers', 'two-sum', 'recursion', 'count-change', 'longest-subsequence', 'koko-eat-bananas', 'movie-ratings', 'N-queens', 'sudoku-solver', 'binary-search', 'edmons-karp', 'bfs', 'dfs', 'greedy', 'sliding-window', 'two-pointer', 'max-flow', 'dinics', 'dijkstra', 'state-space', 'sweep-line', 'bellman-ford', 'floyd-warshall']
names = ["eric-leow", "jimmy-tan", "koh-keira", "guan-yu", "syed", "cheng-xi", "en-le", "Sam"]
python_syntax = [
    "\tx = 10\n",
    "\ty = 'Hello'\n",
    "\tint_var = 10\n",
    "\tfloat_var = 3.14\n",
    "\tstr_var = 'Python'\n",
    "\tbool_var = True\n",
    "\tlist_var = [1, 2, 3]\n",
    "\ttuple_var = (1, 2, 3)\n",
    "\tdict_var = {'a': 1, 'b': 2}\n",
    "\tset_var = {1, 2, 3}\n",
    "\tif x > 5:\n\t\tprint('Greater')\n\telse:\n\t\tprint('Smaller or equal')\n",
    "\tfor i in range(5):\n\t\tprint(i)\n",
    "\tcount = 0\n\twhile count < 5:\n\t\tprint(count)\n\t\tcount += 1\n",
    "\tfor i in range(5):\n\t\tif i == 3:\n\t\t\tbreak\n\t\tprint(i)\n",
    "\tdef greet(name):\n\t\tprint('Hello, ' + name)\n\tgreet('Alice')\n",
    "\tmultiply = lambda x, y: x * y\n\tprint(multiply(2, 3))\n",
    "\tmy_list = [1, 2, 3, 4]\n\tmy_list.append(5)\n\tmy_list.pop()\n\tmy_list[0]\n\tmy_list[1:3]\n",
    "\tstr1 = 'Hello'\n\tstr2 = 'World'\n\tconcatenated = str1 + ' ' + str2\n",
    "\tupper_str = str1.upper()\n\tlower_str = str2.lower()\n\tsubstring = str1[1:4]\n",
    "\tmy_dict = {'a': 1, 'b': 2}\n\tvalue = my_dict['a']\n\tmy_dict['c'] = 3\n\tdel my_dict['b']\n",
    "\ttry:\n\t\tx = 10 / 0\n\texcept ZeroDivisionError:\n\t\tprint('Cannot divide by zero')\n\tfinally:\n\t\tprint('This will always execute')\n",
    "\tclass Person:\n\t\tdef __init__(self, name, age):\n\t\t\tself.name = name\n\t\t\tself.age = age\n\t\tdef greet(self):\n\t\t\tprint(f'Hello, my name is {self.name} and I am {self.age} years old')\n\tperson1 = Person('Alice', 25)\n\tperson1.greet()\n",
    "\tsquares = [x**2 for x in range(5)]\n\teven_numbers = [x for x in range(10) if x % 2 == 0]\n",
    "\twith open('file.txt', 'r') as file:\n\t\tcontent = file.read()\n\t\tprint(content)\n",
    "\twith open('file.txt', 'w') as file:\n\t\tfile.write('Hello, World!')\n",
    "\timport math\n\tprint(math.sqrt(16))\n",
    "\tfrom datetime import datetime\n\tprint(datetime.now())\n",
    "\tmy_list = [1, 2, 3]\n\titerator = iter(my_list)\n\tprint(next(iterator))\n\tprint(next(iterator))\n",
    "\tdef count_up_to(max):\n\t\tcount = 1\n\t\twhile count <= max:\n\t\t\tyield count\n\t\t\tcount += 1\n\tcounter = count_up_to(3)\n\tprint(next(counter))\n\tprint(next(counter))\n",
    "\tdef decorator_function(func):\n\t\tdef wrapper():\n\t\t\tprint('Before the function call')\n\t\t\tfunc()\n\t\t\tprint('After the function call')\n\t\treturn wrapper\n\t@decorator_function\n\tdef say_hello():\n\t\tprint('Hello')\n\tsay_hello()\n",
    "\tdef add_numbers(a: int, b: int) -> int:\n\t\treturn a + b\n\ta, b, c = [1, 2, 3]\n\tprint(a, b, c)\n",
    "\tdict1 = {'a': 1, 'b': 2}\n\tdict2 = {'c': 3}\n\tmerged_dict = {**dict1, **dict2}\n\tprint(merged_dict)\n",
    "\tfor index, value in enumerate(my_list):\n\t\tprint(f'Index {index}: {value}')\n",
    "\tnames = ['Alice', 'Bob', 'Charlie']\n\tscores = [90, 85, 88]\n\tfor name, score in zip(names, scores):\n\t\tprint(f'{name}: {score}')\n",
    "\tx = 10\n\tassert x == 10"
]

script_name = os.path.basename(__file__)

for filename in os.listdir('.'):
    file_path = os.path.join('.', filename)
    
    if os.path.isfile(file_path) and filename != script_name:
        try:
            os.remove(file_path)
            print(f"Deleted {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")

def pad(term):
    if len(str(term)) == 1: return "0" + str(term)
    else: return str(term)

alphabets_and_numbers = list(string.ascii_letters) + list(string.digits) + [" "]

for problem in problem_titles:
    submissions = random.randint(0,10)

    for i in range(submissions):
        year, month, day, hour, minute, second = random.randint(2020, 2024), random.randint(1,12), random.randint(1,28), \
                                             random.randint(0,23), random.randint(0,60), random.randint(0,60)
        with open(f"{problem}_{random.choice(names)}_{year}-{pad(month)}-{pad(day)}-{pad(hour)}-{pad(minute)}-{pad(second)}.txt", "w") as file:
            all_solved = True if random.randint(0,8) == 1 else False
            none_solved = True if random.randint(0,8) == 2 else False
            total = random.randint(1, 80)
            solved = total if all_solved else 0 if none_solved else random.randint(0, total)
            file.write(f"Number of test cases passed: {solved}/{total}\n")

            functions = random.randint(1, 6)
            for j in range(functions):
                length = random.randint(1,25)
                function_name = "".join([chr(random.randint(0,25) + ord('a')) for j in range(length)])
                length = random.randint(0,5)
                params = []
                for s in range(length):
                    param_length = random.randint(1,5)
                    str_build = [chr(random.randint(0,25) + ord('a')) for j in range(param_length)]
                    params.append("".join(str_build))
                file.write(f"var {function_name} = ({", ".join(params)}) => " + "{\n")
                lines = random.randint(0, 10)
                for k in range(lines):
                    file.write(f"{random.choice(python_syntax)}\n")
                file.write(f"\treturn {''.join([random.choice(alphabets_and_numbers) for l in range(random.randint(1,10))])}\n")
                file.write("}\n\n")
                    
            
