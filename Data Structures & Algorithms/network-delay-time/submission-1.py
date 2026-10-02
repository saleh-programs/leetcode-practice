class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # create vertices list and adjacency list
        unvisited = set()
        adj_list = defaultdict(list)
        for i in range(1, n+1):
            unvisited.add(i)
            adj_list[i] = []
        for i in range(len(times)):
            adj_list[times[i][0]].append([times[i][1], times[i][2]])
        
        # tracking path costs
        costs = {
            i: float("inf") for i in unvisited
        }
        costs[k] = 0

        current = None
        path = 0
        while unvisited:
            # replace with heap later
            smallest = float("inf")
            for v, cost in costs.items():
                if v in unvisited and cost <= smallest:
                    smallest = cost
                    current = v
            path = costs[current]

            # update neighbors
            for nbr in adj_list[current]:
                costs[nbr[0]] = min(costs[nbr[0]], path + nbr[1])

            # mark current node
            unvisited.remove(current)
        
        res = float("-inf")
        for v, cost in costs.items():
            res = max(res, cost)
        if (res == float("inf")):
            return -1


        return res

            


        