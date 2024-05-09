import json
"""
x = open("routine_walkthrough/routines.json", "r")
#y = json.loads(x)
y = json.loads(x.read())
print(y)
print("first test")
print(y['routines'][0]['morning'][0]['get dressed']) #This is how to properly read the .json file and organize it
print("second test")
print(type(y['routines'][0]['morning'][0]['get dressed']))
print("third test")
"""
#y['routines'][0][i] this is how I will process the individual routines.

class routine_control():# create different objects for each routine than save them as different objects if this
    def __init__(self):
        super().__init__()

        self.routines = self.get_routines()

    def breakdown_into_list(self):#don't need this other class's job
        pass

    def update_routine(self):#constantly update the routine from changes made in the routine viewer
        pass#might move this

    def rebuild_routine(self):#receive the "routine" from the routine viewer and formulate/rebuild it
        pass
        
class back_end_setup():
    def __init__(self, num):#currently using this to verify it works
        super().__init__()
        self.routines = self.get_routines()
        print(type(list(self.routines)))
        #self.routines = list(self.routines)
        print(type(self.routines))
        self.separate_routine(self.routines, num)
        print("temp")
        temp = self.get_specific_routine(num)
        self.routine = temp
        print(temp)
        print("temp")
        temp = self.get_specific_routine(1)
        print(temp)
        """self.keyholder = []
        for i in temp:
            self.keyholder.append(i)
            print(i)"""
        self.keyholder = self.get_keyholder(self.routine)
        print(self.keyholder[num])
        print(self.routine[self.keyholder[num]])

    def get_routines(self):
        x = open("routine_walkthrough/routines.json", "r")
        print(x)
        self.all_routines = json.loads(x.read())
        print(self.all_routines)
        return self.all_routines['routines'][0]

    def separate_routine(self, x, z):
        print(x)
        #print(x[0])
        self.routines_list = []
        for y in x:
            print(type(y))
            self.routines_list.append(self.routines[y][0])
        print(str(self.routines_list)+str(z))
        print(self.routines_list[0])
        for i in self.routines_list:
            print(z)
            print(i)
    
    def get_keyholder(self, x):
        temporary_keyholder = []
        for i in x:
            temporary_keyholder.append(i)
            print(i)
        return temporary_keyholder
    
    def get_specific_routine(self, n):
        return self.routines_list[n]
        


    def rebuild_all_routines(self, x):
        print("testing")
        print(x[0])
        print(self.temp[x[0]])
        #pass

    def save_routines(self):
        self.all_routines
        
        return

test = back_end_setup(0)
print(test.save_routines())