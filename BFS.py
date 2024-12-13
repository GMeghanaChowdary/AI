#BFS 
tree ={ 
1: [2,9,10], 
2: [3,4], 
3: [],
4: [5,6,7], 
5: [8], 
6: [], 
7: [], 
8: [], 
9: [], 
10: [] 
} 
def breadth_first_search(tree,start): 
    q=[start] 
    visited=[]  
    while q: 
        print("before",q) 
        node=q.pop(0) 
        visited.append(node) 
        for child in (tree[node]): 
            if child not in visited and child not in q: 
                q.append(child) 
        print("after",q) 
    return visited 
result=breadth_first_search(tree,1) 
print(result)
