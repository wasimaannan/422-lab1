f1=open("input.txt","r")
inp=f1.readlines()

import math

h_table={} #heuristic table using dictionary
pred_list={} #predecessor list to keep track of parent nodes
graph={}

for x in inp:
    line=x.strip().split()
    h_table[line[0]]=int(line[1]) #retrieving heuristic values and storing in dictionary
    c_nodes=[]
    for y in range(2,len(line),2):
        c_nodes+=[[line[y],int(line[y+1])]] #a nested list of child nodes and cost
    graph[line[0]] = {"neigbors": c_nodes,"distance": math.inf} #making a graph using dictionary


for key,value in h_table.items(): #assigning goal node from heuristic table
    if value==0:
        goal_node=key

import heapq as priority_queue

source=input("Start node:")
dest=input("Destination:")

if source and dest in h_table:
    if dest==goal_node:
        dest=goal_node


    Q=[(h_table[source],source,0)]
    tracker={}

    while len(Q)!=0:
        h,node,starting_cost=priority_queue.heappop(Q)

        if node!=dest:
            tracker[node]=True
            for key,value in graph[node].items():
                if key=="neigbors":
                    for neighbor in value:
                        child=neighbor[0]
                        path_cost=neighbor[1]
                        if child not in tracker:
                            total_cost = starting_cost + path_cost + h_table[child] 
                            if total_cost < graph[child]["distance"]:
                                graph[child]["distance"] = total_cost #updating the costs of each node
                                pred_list[child]=node #updating the parent list
                                priority_queue.heappush(Q, (total_cost, child, starting_cost + path_cost))
        else:
            break

    if dest!=goal_node:
        graph[dest]['distance']=graph[dest]['distance']-h_table[dest] 
        #Assigning heuristic 0 to destination. Otherwise, cost is wrong
    
    if node == dest:
        curr=dest
        route= []
        while curr != source:
            route+=[curr]
            curr =pred_list[curr]
        route.append(source)
        s="Path: "
        for nodes in range(len(route)-1,0,-1):
            s+=f"{route[nodes]} -> "
        s+=route[0]
        print(s)
        print(f"Total distance: {graph[dest]['distance']} km")
    else:
        print("NO PATH FOUND")
    
else:
    print("NO PATH FOUND")

f1.close()