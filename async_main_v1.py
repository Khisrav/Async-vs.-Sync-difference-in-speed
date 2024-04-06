import time, os, asyncio, aiohttp, aiofiles

BASE_URL = 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/995373701759c93909be840805690e1a/onepunch_man_202_{}.jpg'
TOTAL_PAGES = 12

async def get_pic(i):
    pass

async def get_pics(session, i):
    async with session.get(i) as response:
        filename = os.path.basename(f'{i}')
        print(f'Downloading pic {filename}')

        if response.status == 200:
            f = await aiofiles.open(f'onepunchman/{filename}', mode='wb')
            await f.write(await response.read())
            await f.close()

        return await response.release()

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


async def main(loop):
    urls = [BASE_URL.format(i) for i in range(1, TOTAL_PAGES + 1)]

    async with aiohttp.ClientSession(headers={'User-agent': 'google'}) as session:
        tasks = [get_pics(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

    print(f'Time: {time.time() - start_time}')

    remove_files('onepunchman')