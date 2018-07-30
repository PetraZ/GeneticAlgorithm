# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:36:22 2018

@author: lenovo
"""
import numpy as np
import string

class GA():
    def __init__(self,target):
        self.target = target
        self.pops = []
        self.first_generation(10)
        
    def fitness(self,trial):
        return sum(i==j for i,j in zip(self.target,trial))
    
    def first_generation(self,pop):
        for i in range(pop):
            new_one = ''.join(np.random.choice(list(string.ascii_letters)) for _ in range(len(self.target)))
            self.pops.append((new_one,self.fitness(new_one)))
            
    def crossover(self,pops=20):
        self.pops = sorted(self.pops,key=lambda x:x[1],reverse=True)[:20]
        
        for pop in range(pops):
            parent_1 = self.pops[np.random.randint(10)]
            parent_2 = self.pops[np.random.randint(10)]
            
            point =  np.random.randint(len(self.target))
            new_one = parent_1[0][:point]+parent_2[0][point:]
#            print (new_one)
            new_one = self.mutate(new_one)
            self.pops.append((new_one,self.fitness(new_one)))
            
    def mutate(self,item,probability=0.05):
        new_one = ''
        for char in item:
            flag = np.random.choice([1,0],p=[0.05,0.95])
            if flag:
                new_one += np.random.choice(list(string.ascii_letters))
            else:
                new_one += char
        return new_one
    
    def run(self,iters):
        for i in range(iters):
            self.crossover(pops=20)
        return sorted(self.pops,key=lambda x:x[1],reverse=True)[0]

target= list("PETERYIANGNEVERGIVEUP")
a = GA(target)
print(a.run(500))
