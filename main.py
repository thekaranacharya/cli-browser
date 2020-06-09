import sys
import os

browser_history = []
urls = ['nytimes.com', 'bloomberg.com']

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow
and change shape, and that could be a boon to medicine
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's
 Bad Moon Rising. The world is a very different place than
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# function to read the contents of the web page
def read_contents(page_url):
    if os.path.exists(dir_path + '/' + page_url):
        file_path = os.path.join(dir_path, page_url)
        page = open(file_path, 'r')
        print(page.read())
        page.close()
    else:
        print('Error: Incorrect URL')

# function to write the contents into a file
def write_contents(page_file):
    file_path = os.path.join(dir_path, page_file)
    web_page = open(file_path, 'w')
    web_page.write(eval(command.replace('.', '_')))
    web_page.close()

# function to save a webpage to a directory in a file
def save_page(url):
    file_name = url.rstrip('.com')

    # open the page in write mode at the specified path and write it's contents
    write_contents(file_name)

    # append current page to browser history
    browser_history.append(file_name)

    # print the contents of the page
    print(eval(command.replace('.', '_')))

# function to mimic the 'back' button of a browser
def go_back():
    # check if the stack contains at least 2 elements
    # i.e. current page & a page to return to
    if len(browser_history) > 1:
        browser_history.pop()  # pop the current page you're on
        page_to_load = browser_history[-1]  # last in, first out

        # open the page in read mode and print the contents
        read_contents(page_to_load)

# ------------------ main program execution starts here ---------------------------
# command line argument (directory name)
dir_name = sys.argv[1]

root_dir = os.getcwd()
dir_path = root_dir + '/' + dir_name
if not os.path.exists(dir_path):  # if only the directory doesn't exist already
    os.mkdir(dir_name)

while True:
    command = input()
    if command in urls:
        save_page(command)
    elif command == 'back':
        go_back()
    else:
        if command == 'exit':
            break
        else:
            read_contents(command)