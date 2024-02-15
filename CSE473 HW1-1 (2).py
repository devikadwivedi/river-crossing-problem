start = (3, 3, 'L')
path = []
visited = []  # stack
illegal_count = 0
repeat_count = 0
total_count = 0


# searches for the winning paths of missionary and cannibals
# takes the current state (current_state), pathway to the current state (path), and visited states (visited)
#
def dfs(curr_state, path, visited):
  if (curr_state not in visited):
    # check if goal state
    if is_goal(curr_state):
      print_solution(path)
      return
    # generate list L of successors
    L = generate_successors(curr_state)
    # calling itself recursively for each state in L
    for state in L:
      path.append(curr_state)
      visited.insert(0, curr_state)
      dfs(state, path, visited)
      path.pop(-1)
      visited.pop()
  return


# returns a list of all the legal successor states given the current state (state)
def generate_successors(state):
  m, c, s = state
  L = []

  for i in range(3):
    for j in range(3):
      if (i + j <= 2 and i + j > 0):
        if s == 'L':
          new_state = (m - i, c - j, "R")
        else:
          new_state = (m + i, c + j, "L")
        if (is_legal(new_state)):
          L.append(new_state)
  return L


#checks if goal has been reached: ie everyone is on the right side
def is_goal(state):
  m, c, s = state
  return (m == 0 and c == 0 and s == "R")

# checks that the state is legal and unvisited
def is_legal(state):
  global illegal_count, total_count, repeat_count, visited
  m, c, s = state
  # check that missionaries are not dead
  if (m > 0 and m < c):
    illegal_count += 1
    return False
  if (m < 3 and c < m):
    illegal_count += 1
    return False
  # check other invalid states and whether the state has been visited
  if (m < 0 or c < 0 or m > 3 or c > 3):
    return False
  if (state in visited):
    repeat_count += 1
    return False
  total_count += 1
  return True

def print_solution(path) :
  solution = ""
  for item in path:
    solution += "(" + str(item[0]) + "," + str(item[1]) + "," + str(item[2]) + ")"
  solution +="(0,0,R)"
  print(solution)

dfs(start, path, visited)
print(total_count)
print(repeat_count)
print(illegal_count)