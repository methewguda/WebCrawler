import os

# Each website you crawl is a separate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.mkdir(directory)

create_project_dir('methewguda')