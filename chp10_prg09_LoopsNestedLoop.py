#Show the way that nested loop works
for loop in range (1,10+1): #Main loop
    print("Main loop", loop)
    for nested_loop in range (1,5+1): #Nested loop       
        print("   Nested loop", nested_loop)
