import os

# Each website you crawl is a separate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.mkdir(directory)

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Create a new file
def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()

# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        file.close()

# Delete the content of a file
def delete_file_content(path):
    with open(path, 'w'):
        pass