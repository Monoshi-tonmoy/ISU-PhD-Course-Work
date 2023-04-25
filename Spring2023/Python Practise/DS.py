#mylist=[1,2,34,5,6,7]

#print(mylist[::-1])

mydict={};

print("How many entries do you need?");
num_input=input();

num_input=int(num_input);

for i in range(num_input):
    key=input();
    value=input();

    mydict[key]=value;

print(mydict);