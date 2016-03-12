(lambda N:(lambda N,A:print(("Average: %.2f\n"%A)+str([n for n in N if len(n)>A])))(N,sum([len(n)for n in N])/len(N)))([n.strip()for n in __import__("sys").stdin])
