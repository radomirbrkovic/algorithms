def criticalRouters(numRouters, numLinks, links):
    linksCounter = {}
    for link in links:
        linksCounter[link[0]] = countChildren(links, link[0])
        links.remove(link)

    return linksCounter    

def countChildren(graph, node):
    result = 0;

    for edge in graph:
        print str(edge[0]) +" "+str(node)
        if edge[0] == node:
            result += countChildren(graph, edge[1]) + 1

    return result; 


links1  = [ [1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4, 5] ]

print criticalRouters(7, 7, links1)