import os

my_dir = os.getcwd()
for root, dirnames, fnames in os.walk(my_dir):
    for fname in fnames:
        if fname.count('.'): continue  # don't process a file with an extension
        os.rename(os.path.join(root, fname), os.path.join(root, "{}.png".format(fname)))
        
