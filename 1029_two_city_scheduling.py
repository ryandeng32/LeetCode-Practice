# Goal: Assign exactly N candidate to city A & N to city B
# Minimize travel cost

''' main takeaways: 
    questions like this is like a sorting problem, so I should figure out what parameter should be sorted
    in this case it's the difference between costs to A and B 
'''


# will sorting work?
# no, because we want to balance cost to A & B, so sorting either by A or B will not work

# actual parameter we want to minimize is how much we will benefit if we choose to go to A or B
# so the difference between the costs

# my first solution
def twoCitySchedCost(costs):
    total = 0
    diff = [abs(i[0] - i[1]) for i in costs]
    A = 0
    B = 0
    N = len(costs) / 2
    while A + B != 2 * N:
        index = diff.index(max(diff))
        cost = costs[index]
        city = cost.index(min(cost))
        if A != N and city == 0:
            A += 1
            total += cost[city]
        elif B != N and city == 1:
            B += 1
            total += cost[city]
        else:
            if city == 1:
                A += 1
                total += cost[0]
            else:
                B += 1
                total += cost[1]
        diff.pop(index)
        costs.pop(index)
    return total
# what can be improved?
# no need to use absolute value, so A, B weren't needed as well

# code improved:


def new_twoCitySchedCost(costs):
    sorted_cost = sorted(costs, key=lambda x: x[0]-x[1])
    result = 0
    for i in range(len(costs)):
        if i < len(costs) / 2:
            result += sorted_cost[i][0]
        else:
            result += sorted_cost[i][1]
    return result
