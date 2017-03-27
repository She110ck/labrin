import os

def print_directory_contents(sPath):
    """ 
    elbette ki bu walk funksiyasini tamam imitasiya etmir, ama telebleri odeyir
    """
    for i in os.listdir(sPath):
        if os.path.isdir(os.path.join(sPath,i)):
            print('d' , sPath)
            print_directory_contents(os.path.join(sPath,i))
        else:
            print('f',os.path.join(sPath,i))

path = os.getcwd()
print_directory_contents(path)
