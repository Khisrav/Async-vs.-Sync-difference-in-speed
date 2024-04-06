import requests, time, os, shutil
from bs4 import BeautifulSoup

BASE_URL = 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/995373701759c93909be840805690e1a/onepunch_man_202_{}.jpg'
TOTAL_PAGES = 12

def get_pic(i):
    print(f'Downloading pic {i}')
    r = requests.get(BASE_URL.format(i), stream=True)
    if r.status_code == 200:
        with open(f'onepunchman/{i}.jpg', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def get_pics():
    for  i in range(1, TOTAL_PAGES+1):
        get_pic(i)

def main():
    get_pics()

def remove_files(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Iterate over all files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                # If it's a file, remove it
                os.remove(file_path)
        except Exception as e:
            print(f"Error while deleting {file_path}: {e}")

if __name__ == '__main__':
    start_time = time.time()

    if os.path.isdir('onepunchman') == False:os.mkdir('onepunchman')

    main()

    print('Time: {}'.format(time.time() - start_time))
    
    remove_files('onepunchman')