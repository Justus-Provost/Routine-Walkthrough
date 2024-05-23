import json

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
        print(type(self.routines))
        self.separate_routine(self.routines, num)
        print("temp")
        temp = self.get_specific_routine(num)
        self.routine = temp
        print(temp)
        print("temp")
        temp = self.get_specific_routine(1)
        print(temp)
        self.keyholder = self.get_keyholder(self.routine)
        # print(self.keyholder[num])
        # print(self.routine[self.keyholder[num]])
        self.num = num

    def get_routines(self):
        x = open("routine_walkthrough/routines.json", "r")
        print(x)
        self.all_routines = json.loads(x.read())
        print(self.all_routines)
        x.close()
        return self.all_routines['routines'][0]

    def separate_routine(self, x, z):
        print(x)
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

    def save_routines(self, test):
        y = []
        for i in self.all_routines['routines'][0]:
            y.append(i)
        #self.all_routines['routines'][0] = test
        #self.routines[self.all_routines['routines'][0][self.num]][0] = test
        #self.routines[self.routines_list[self.num]]
        # print("routine list type: "+str(type(self.routines_list)))
        # print("routine list[] type: "+str(type(self.routines_list[self.num])))
        # self.routines_list[self.num] = test
        # print("routine list: "+str(self.routines_list))
        # print("routine list: "+str(self.routines_list[self.num]))
        # x = open("routine_walkthrough/routines.json", "r")
        # print(x)
        # self.all_routines = json.loads(x.read())
        # print(self.all_routines)
        # x.close()
        print(str(self.all_routines['routines'][0][y[self.num]][0]))
        self.all_routines['routines'][0][y[self.num]][0] = test
        print(str(self.all_routines['routines'][0][y[self.num]][0]))
        print(str(self.all_routines))
        print("the json")
        x = open("routine_walkthrough/routines.json", "w")
        print(x)
        y = json.dumps(self.all_routines, indent=4)#, separators=", ")

        #self.all_routines = json.loads(x.read())
        print(y)
        x.write(y)
        # print("received"+str(test))
        # print("rebuilt"+str(self.all_routines))
        # print("maybe"+str(self.routines))
