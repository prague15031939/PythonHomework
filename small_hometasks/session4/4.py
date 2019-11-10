a = "I am global variable!"

def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():
        
        #a = "I am local variable!"
        #global a
        print(a)
    
    inner_function()
                
enclosing_function()  