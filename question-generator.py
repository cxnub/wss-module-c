import random


problems = [
     {
        "title": "add-two-numbers", 
        "description": "Given two numbers, return their sum.", 
        "difficulty": 2.5, 
        "setter": "Eric", 
        "submissions": 45000, 
        "commonality": "common", 
        "author": "LeetCode", 
        "example_problem_title": "Sum of Two Numbers",
        "problem_statement": "Given two numbers, a and b, return their sum.\nThe inputs will be between 0 and 100000 (inclusive).",
        "examples": [
            "Given a = 3 and b = 2, return 5.",
            "Given a = 0 and b = 0, return 0.",
            "Given a = 100000 and b = 50000, return 150000."
        ]
    },

    {
        "title": "subtract-two-numbers", 
        "description": "Given two numbers, return the result of subtracting the second number from the first.", 
        "difficulty": 2.0, 
        "setter": "Jim", 
        "submissions": 30000, 
        "commonality": "common", 
        "author": "LeetCode", 
        "example_problem_title": "Subtract Two Numbers",
        "problem_statement": "Given two numbers, a and b, return their difference a - b.\nThe inputs will be between 0 and 100000 (inclusive).",
        "examples": [
            "Given a = 5 and b = 3, return 2.",
            "Given a = 7 and b = 10, return -3.",
            "Given a = 100000 and b = 50000, return 50000."
        ]
    },

    {
        "title": "two-sum", 
        "description": "Given an array of integers, find two numbers such that their sum equals a target value.", 
        "difficulty": 3.5, 
        "setter": "Timmy", 
        "submissions": 60000, 
        "commonality": "must know!", 
        "author": "LeetCode", 
        "example_problem_title": "Two Sum",
        "problem_statement": "Given an array of integers, nums, and a target value, return the indices of the two numbers that add up to the target.\nThe inputs will be between -10^9 and 10^9 and the array length will not exceed 10^4.",
        "examples": [
            "Given nums = [2, 7, 11, 15] and target = 9, return the indices [0, 1].",
            "Given nums = [3, 2, 4] and target = 6, return the indices [1, 2].",
            "Given nums = [3, 3] and target = 6, return the indices [0, 1]."
        ]
    },

    {
        "title": "recursion", 
        "description": "Solving problems by breaking them down into smaller instances of the same problem, calling the function within itself.", 
        "difficulty": 4.0, 
        "setter": "Eric", 
        "submissions": 20000, 
        "commonality": "common", 
        "author": "Tim Peters", 
        "example_problem_title": "Recursive Fibonacci",
        "problem_statement": "Implement a recursive function that computes the Fibonacci number at position n.\nThe input will be an integer n (0 <= n <= 30).",
        "examples": [
            "Given n = 5, return 5.",
            "Given n = 10, return 55.",
            "Given n = 0, return 0."
        ]
    },

    {
        "title": "count-change", 
        "description": "Given a set of coin denominations, count the number of ways to make change for a given amount.", 
        "difficulty": 5.0, 
        "setter": "Jim", 
        "submissions": 15000, 
        "commonality": "sparse", 
        "author": "Dynamic Programming", 
        "example_problem_title": "Coin Change Problem",
        "problem_statement": "Given a list of coin denominations and an amount, count the number of ways to make change for that amount.\nThe coin denominations are positive integers, and the amount is a non-negative integer.",
        "examples": [
            "Given coins = [1, 2, 5] and amount = 5, return 4.",
            "Given coins = [2] and amount = 3, return 0.",
            "Given coins = [1, 2, 3] and amount = 4, return 4."
        ]
    },

    {
        "title": "longest-subsequence", 
        "description": "Find the longest subsequence of a given sequence that is strictly increasing or satisfies a particular condition.", 
        "difficulty": 6.0, 
        "setter": "Eric", 
        "submissions": 23000, 
        "commonality": "sparse", 
        "author": "LeetCode", 
        "example_problem_title": "Longest Increasing Subsequence",
        "problem_statement": "Given an array of integers, find the length of the longest increasing subsequence.\nThe input array will have at most length 1000.",
        "examples": [
            "Given nums = [10, 9, 2, 5, 3, 7, 101, 18], return 4.",
            "Given nums = [0, 1, 0, 3, 2, 3], return 4.",
            "Given nums = [7, 7, 7, 7, 7, 7], return 1."
        ]
    },

    {
        "title": "koko-eat-bananas", 
        "description": "Given an array of piles of bananas, determine the minimum eating speed Koko must use to finish eating within a certain time limit.", 
        "difficulty": 4.5, 
        "setter": "Timmy", 
        "submissions": 25000, 
        "commonality": "rare", 
        "author": "LeetCode", 
        "example_problem_title": "Koko Eating Bananas",
        "problem_statement": "Koko loves bananas. There are piles of bananas, each pile has a number of bananas. Koko can eat up to k bananas per hour. Determine the minimum k such that she can finish all bananas within h hours.",
        "examples": [
            "Given piles = [3, 6, 7, 11] and h = 8, return 4.",
            "Given piles = [30, 11, 23, 4, 20] and h = 5, return 30.",
            "Given piles = [30, 11, 23, 4, 20] and h = 6, return 23."
        ]
    },

    {
        "title": "movie-ratings", 
        "description": "Given a set of movie ratings, compute the average rating for each movie or filter movies by a specific rating threshold.", 
        "difficulty": 3.0, 
        "setter": "Jim", 
        "submissions": 18000, 
        "commonality": "common", 
        "author": "Movie Database", 
        "example_problem_title": "Movie Rating System",
        "problem_statement": "Given a list of movie ratings, return the average rating for each movie.\nRatings are floating point numbers between 0.0 and 10.0.",
        "examples": [
            "Given ratings = [3.5, 4.0, 2.5, 4.5], return 3.875.",
            "Given ratings = [5.0, 6.5, 7.0, 8.0, 9.0], return 7.0.",
            "Given ratings = [10.0, 10.0, 10.0, 10.0], return 10.0."
        ]
    },

    {
        "title": "N-queens", 
        "description": "Solve the N-Queens problem by placing N queens on an N×N chessboard such that no two queens threaten each other.", 
        "difficulty": 6.5, 
        "setter": "Eric", 
        "submissions": 35000, 
        "commonality": "must know!", 
        "author": "Chess Mathematics", 
        "example_problem_title": "N-Queens Puzzle",
        "problem_statement": "Given an integer n, return all distinct solutions to the n-queens puzzle.\nEach solution must be represented as a list of strings, where '.' and 'Q' represent empty spaces and queens, respectively.",
        "examples": [
            "Given n = 4, return two distinct solutions to the 4-queens puzzle."
        ]
    },
{
        "title": "sudoku-solver", 
        "description": "Given a partially filled 9×9 grid, fill in the grid so that it satisfies the rules of Sudoku (each row, column, and 3x3 subgrid contain all digits from 1 to 9).", 
        "difficulty": 7.0, 
        "setter": "Timmy", 
        "submissions": 30000, 
        "commonality": "common", 
        "author": "Mathematical Logic", 
        "example_problem_title": "Sudoku Solver",
        "problem_statement": "Given a partially filled 9×9 grid, fill in the grid such that each row, each column, and each 3x3 subgrid contains all digits from 1 to 9.",
        "examples": [
            "Given the input grid with some filled numbers, return the filled grid that satisfies Sudoku rules."
        ]
    },

    {
        "title": "binary-search", 
        "description": "Search for a target element in a sorted array using the divide-and-conquer binary search algorithm.", 
        "difficulty": 3.0, 
        "setter": "Jim", 
        "submissions": 55000, 
        "commonality": "must know!", 
        "author": "John Mauchly", 
        "example_problem_title": "Binary Search on Sorted Array",
        "problem_statement": "Given a sorted array of integers, nums, and a target value, search for the target in the array using the binary search algorithm.\nThe inputs will be between -10^9 and 10^9, and the array length will not exceed 10^4.",
        "examples": [
            "Given nums = [1, 2, 3, 4, 5, 6] and target = 4, return the index 3.",
            "Given nums = [1, 3, 5, 7, 9] and target = 2, return -1.",
            "Given nums = [10, 20, 30, 40, 50] and target = 30, return the index 2."
        ]
    },

    {
        "title": "edmons-karp", 
        "description": "An implementation of the Ford-Fulkerson method for computing the maximum flow in a flow network using breadth-first search.", 
        "difficulty": 7.5, 
        "setter": "Timmy", 
        "submissions": 10000, 
        "commonality": "rare", 
        "author": "Edmonds & Karp", 
        "example_problem_title": "Maximum Flow Problem",
        "problem_statement": "Implement the Edmonds-Karp algorithm to find the maximum flow in a flow network using BFS.\nThe graph will have a set of nodes and edges with capacities.",
        "examples": [
            "Given a flow network, return the maximum flow from source to sink."
        ]
    },

    {
        "title": "bfs", 
        "description": "Breadth-first search algorithm for traversing or searching through a graph or tree, visiting nodes level by level.", 
        "difficulty": 4.0, 
        "setter": "Eric", 
        "submissions": 50000, 
        "commonality": "common", 
        "author": "C. L. A. S. A.", 
        "example_problem_title": "Breadth First Search",
        "problem_statement": "Given a graph represented by an adjacency list, implement the breadth-first search (BFS) algorithm to traverse the graph or search for a target node."
    },

    {
        "title": "dfs", 
        "description": "Depth-first search algorithm for exploring a graph or tree by going deep into the nodes before backtracking.", 
        "difficulty": 4.5, 
        "setter": "Jim", 
        "submissions": 45000, 
        "commonality": "common", 
        "author": "Charles Babbage", 
        "example_problem_title": "Depth First Search",
        "problem_statement": "Given a graph represented by an adjacency list, implement the depth-first search (DFS) algorithm to explore the graph.",
        "examples": [
            "Given a graph, explore it by visiting nodes as deeply as possible before backtracking."
        ]
    },

    {
        "title": "greedy", 
        "description": "A class of algorithms that make the locally optimal choice at each step, with the hope of finding a global optimum.", 
        "difficulty": 6.0, 
        "setter": "Timmy", 
        "submissions": 40000, 
        "commonality": "must know!", 
        "author": "Various Authors", 
        "example_problem_title": "Greedy Algorithm Problems",
        "problem_statement": "Solve optimization problems by selecting the locally optimal choices at each step, with the goal of finding the global optimum."
    },

    {
        "title": "sliding-window", 
        "description": "A technique for solving problems involving arrays or lists by using a window that slides over the data to reduce time complexity.", 
        "difficulty": 5.0, 
        "setter": "Eric", 
        "submissions": 30000, 
        "commonality": "common", 
        "author": "LeetCode", 
        "example_problem_title": "Sliding Window Maximum",
        "problem_statement": "Given an array of integers and an integer k, find the maximum value in each sliding window of size k.",
        "examples": [
            "Given nums = [1, 3, -1, -3, 5, 3, 6, 7] and k = 3, return [3, 3, 5, 5, 6, 7]."
        ]
    },

    {
        "title": "two-pointer", 
        "description": "A technique used to solve problems involving arrays or lists where two pointers move toward each other or from opposite ends to optimize search or sorting.", 
        "difficulty": 4.5, 
        "setter": "Jim", 
        "submissions": 35000, 
        "commonality": "common", 
        "author": "LeetCode", 
        "example_problem_title": "Two Pointers Problem",
        "problem_statement": "Given a sorted array of integers, use the two-pointer technique to solve the problem efficiently.",
        "examples": [
            "Given nums = [1, 2, 3, 4, 5] and target = 6, return the pair [1, 5].",
            "Given nums = [-1, 0, 1, 2, -1, -4] and target = 0, return all unique triplets that sum up to 0."
        ]
    },

    {
        "title": "max-flow", 
        "description": "A flow network problem where the goal is to find the maximum flow from a source node to a sink node.", 
        "difficulty": 7.0, 
        "setter": "Timmy", 
        "submissions": 12000, 
        "commonality": "rare", 
        "author": "L.R. Ford & D.R. Fulkerson", 
        "example_problem_title": "Maximum Flow Problem",
        "problem_statement": "Given a flow network, determine the maximum flow from the source node to the sink node using an appropriate algorithm.",
        "examples": [
            "Given a network of pipes and flow capacities, return the maximum flow from the source to the sink."
        ]
    },

    {
        "title": "dinics", 
        "description": "An optimized algorithm for solving the maximum flow problem, based on layered networks and blocking flows.", 
        "difficulty": 7.5, 
        "setter": "Eric", 
        "submissions": 8000, 
        "commonality": "extremely rare", 
        "author": "Dinic", 
        "example_problem_title": "Dinic's Algorithm for Maximum Flow",
        "problem_statement": "Implement Dinic's algorithm to solve the maximum flow problem using layered networks and blocking flows.",
        "examples": [
            "Given a flow network, implement Dinic's algorithm to calculate the maximum flow."
        ]
    },

    {
        "title": "dijkstra", 
        "description": "An algorithm for finding the shortest paths between nodes in a graph with non-negative edge weights.", 
        "difficulty": 5.0, 
        "setter": "Jim", 
        "submissions": 60000, 
        "commonality": "must know!", 
        "author": "Edsger Dijkstra", 
        "example_problem_title": "Dijkstra's Shortest Path Algorithm",
        "problem_statement": "Given a weighted graph with non-negative edge weights, implement Dijkstra's algorithm to find the shortest path from a source node to all other nodes."
    },

    {
        "title": "state-space", 
        "description": "A search technique where all possible states are considered and explored to find an optimal solution to a problem.", 
        "difficulty": 6.5, 
        "setter": "Eric", 
        "submissions": 7000, 
        "commonality": "rare", 
        "author": "Artificial Intelligence", 
        "example_problem_title": "State-Space Search",
        "problem_statement": "Given a problem, explore the state-space tree to find an optimal solution."
    },
{
        "title": "sweep-line", 
        "description": "A computational geometry technique for solving problems by imagining a vertical line sweeping across the plane and processing events.", 
        "difficulty": 6.0, 
        "setter": "Eric", 
        "submissions": 10000, 
        "commonality": "rare", 
        "author": "Geometry Researchers", 
        "example_problem_title": "Interval Scheduling Maximization",
        "problem_statement": "Given a set of intervals, find the maximum number of non-overlapping intervals that can be scheduled using a sweep-line algorithm.",
        "examples": [
            "Given intervals [(1, 3), (2, 4), (3, 5), (5, 6)], return the maximum number of non-overlapping intervals (which is 3)."
        ]
    },

    {
        "title": "bellman-ford", 
        "description": "An algorithm for finding the shortest paths from a single source node to all other nodes in a graph, even with negative edge weights.", 
        "difficulty": 6.0, 
        "setter": "Jim", 
        "submissions": 35000, 
        "commonality": "common", 
        "author": "Richard Bellman", 
        "example_problem_title": "Bellman-Ford Shortest Path Algorithm",
        "problem_statement": "Given a weighted directed graph, find the shortest paths from a source node to all other nodes. The graph may have negative edge weights but no negative weight cycles.",
        "examples": [
            "Given a graph with edges [(0, 1, 5), (0, 2, 3), (1, 2, 2), (1, 3, 1)], return the shortest paths from node 0 to all other nodes."
        ]
    },
    {
        "title": "floyd-warshall", 
        "description": "An algorithm for finding the shortest paths between all pairs of nodes in a graph, handling both positive and negative weights.", 
        "difficulty": 6.5, 
        "setter": "Timmy", 
        "submissions": 20000, 
        "commonality": "rare", 
        "author": "Robert W. Floyd", 
        "example_problem_title": "Floyd-Warshall All-Pairs Shortest Path",
        "problem_statement": "Given a weighted directed graph, find the shortest paths between all pairs of nodes using the Floyd-Warshall algorithm.",
        "examples": [
            "Given a graph with edges [(0, 1, 3), (0, 2, 8), (1, 2, -4), (2, 3, 7)], return the shortest paths from each node to all other nodes."
        ]
    }
]


def get_one_permutation(lst):
    permuted_lst = lst[:]
    random.shuffle(permuted_lst)
    return permuted_lst

threshold = 3
for problem in problems:
    with open(f"{problem['title']}.txt", "w") as file:
        file.write("---\n")
        new_title = " ".join(list(map(lambda x: x[0].upper() + x[1:], problem['title'].split("-"))))
        fields = [f"Title: {new_title}", f"Description: {problem['description']}"]
        permutation = get_one_permutation(fields)
        for term in permutation:
            file.write(term + "\n")
        other_fields = []
        for field in problem:
            if field not in ["title", "description", "problem_statement", "examples"]:
                parse = f"{field[0].upper() + field[1:].lower()}: {problem[field]}\n"
                can = random.randint(0,10)
                if can <= threshold: file.write(parse)
        file.write("---\n")

        file.write(problem["problem_statement"] + "\n\n")
        if "examples" in problem:
            examples = problem["examples"]
            for example in examples:
                file.write("Example:\n")
                file.write(example + "\n\n")

        
others = [
    {
        "title": "kahns-algorithm",
        "html_content": """
        <h2>Problem Statement</h2>
        <p>Implement Kahn's algorithm for topological sorting of a directed acyclic graph (DAG). The algorithm uses the concept of in-degrees to process nodes in the correct order.</p>
        <p>Given a directed graph, return a topological ordering of the nodes, or report that a cycle exists.</p>
        <h3>Example</h3>
        <ul>
            <li>Given a graph with edges [(0, 1), (0, 2), (1, 3), (2, 3)], return the topological order [0, 1, 2, 3].</li>
            <li>Given a graph with edges [(0, 1), (1, 2), (2, 0)], return that the graph contains a cycle.</li>
        </ul>
        """
    },

    {
        "title": "convex-hull",
        "html_content": """
        <h2>Problem Statement</h2>
        <p>Given a set of points in a 2D plane, find the convex hull of the set, which is the smallest convex polygon that contains all the points.</p>
        <p>Use algorithms such as Graham's scan or Andrew's monotone chain to find the convex hull.</p>
        <h3>Example</h3>
        <ul>
            <li>Given points [(1, 1), (2, 5), (3, 3), (5, 3), (3, 1), (4, 4)], return the convex hull in the form of a set of points forming the polygon.</li>
        </ul>
        """
    },

    {
        "title": "postfix-expression-evaluation",
        "html_content": """
        <h2>Problem Statement</h2>
        <p>Given a postfix expression, evaluate the result. A postfix expression is one where operators follow their operands.</p>
        <p>Use a stack to evaluate the expression, pushing operands and applying operators as they appear.</p>
        <h3>Example</h3>
        <ul>
            <li>Given the postfix expression "2 3 + 5 *", return 25.</li>
            <li>Given the postfix expression "3 4 + 2 *", return 14.</li>
        </ul>
        """
    },

    {
        "title": "computational-geometry",
        "html_content": """
        <h2>Problem Statement</h2>
        <p>Implement algorithms from computational geometry to solve problems such as finding the intersection of lines, convex hull, and closest pair of points.</p>
        <p>Use well-known geometric algorithms to perform tasks like checking if a point is inside a polygon or calculating the area of a polygon.</p>
        <h3>Example</h3>
        <ul>
            <li>Given the points of a polygon [(1, 1), (2, 2), (3, 1)], calculate its area.</li>
        </ul>
        """
    },

    {
        "title": "pre-calculation",
        "html_content": """
        <h2>Problem Statement</h2>
        <p>Some problems require pre-calculation of results for optimization purposes. In this problem, pre-calculate all possible combinations or results within given constraints, and then use these pre-calculated results for efficient query answering.</p>
        <h3>Example</h3>
        <ul>
            <li>Given a range [1, 100], pre-calculate the sum of all integers for each query in the range.</li>
        </ul>
        """
    },

    {
        "title": "modified-dijkstra",
        "html_content": """
        <h2>Problem Statement</h2>
        <p>Implement a modified version of Dijkstra's algorithm that can handle dynamic edge weights and negative weights (though still with no negative cycles).</p>
        <p>The algorithm should return the shortest paths from a source node to all other nodes, with modifications to handle updates in real-time.</p>
        <h3>Example</h3>
        <ul>
            <li>Given a graph with nodes and edges, find the shortest paths from a source node using a modified version of Dijkstra.</li>
        </ul>
        """
    },

    {
        "title": "tarjans-algorithm",
        "html_content": """
        <h2>Problem Statement</h2>
        <p>Implement Tarjan's algorithm to find the strongly connected components (SCCs) in a directed graph. Tarjan's algorithm uses depth-first search (DFS) to find and output all SCCs.</p>
        <p>Given a directed graph, return a list of SCCs where each SCC is a list of nodes that form a strongly connected component.</p>
        <h3>Example</h3>
        <ul>
            <li>Given a graph with edges [(0, 1), (1, 2), (2, 0), (3, 4)], return the strongly connected components: [[0, 1, 2], [3, 4]].</li>
        </ul>
        """
    }
]


for problem in others:
    with open(f"{problem['title']}.html", "w") as file:
        file.write(problem["html_content"] + "\n")








        
        
