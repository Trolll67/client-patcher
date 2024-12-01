import asyncio
from io import BufferedReader
import os
import struct
import sys
import aiohttp
import aiofiles


class BinaryReader():
    """General BinaryReader class"""
    def __init__(self, inputFile: BufferedReader):
        self.inputFile: BufferedReader = inputFile
        self.endian = '<'
        self.debug = False
        self.mode = self.inputFile.mode if hasattr(self.inputFile, 'mode') else None
          
    def read_int32(self) -> int:
        if self.mode != 'rb':
            return None
		
        data = self.inputFile.read(4)
        return struct.unpack(self.endian+'i', data)[0]


def progress_bar(iteration, total, bar_length=50):
	progress = (iteration / total)
	arrow = '=' * int(round(bar_length * progress))
	spaces = ' ' * (bar_length - len(arrow))

	sys.stdout.write(f'\r[{arrow}{spaces}] {int(progress * 100)}% ({iteration}/{total})')
	sys.stdout.flush()

async def download_file(url, filepath) -> bool:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # check status code
            if response.status != 200:
                return False

            content = await response.read()
            async with aiofiles.open(filepath, 'wb') as f:
                await f.write(content)

    return os.path.exists(filepath)


async def main():
    curr_major_version = 2
    curr_patch_version = 1 # load patches from 1 to latest
    curr_minor_version = 15
    
    # Korea
    base_url = 'http://patch-gkr.r2.webzen.co.kr'
    base_path = 'Patches/Korea'
    url_dir = 'r2/test'

    load_files = [
        'R2PatchClient_#ver#.ver',
        'R2PatchClient_#ver#.zip',
        'R2PatchRes_#ver#.rdb',
        'R2PatchRes_#ver#.zip',
    ]

    if not os.path.exists(base_path):
        os.makedirs(base_path)

    url = f'{base_url}/{url_dir}/R2VerData.dat'
    filepath = f'{base_path}/R2VerData.dat'

    print(f'Download {url}...')

    if await download_file(url, filepath):
        with open(filepath, 'rb') as f:
            reader = BinaryReader(f)
            major_version = reader.read_int32()
            patch_version = reader.read_int32()
            minor_version = reader.read_int32()

            print(f'Version: {major_version}.{patch_version}.{minor_version}')

            if curr_patch_version >= patch_version:
                print('No updates available')
                return

            total_patches = patch_version - curr_patch_version
            print(f'Download {total_patches} patches...\n')

            while curr_patch_version + 1 <= patch_version:
                curr_patch_version += 1 # next patch version
                patch_folder = f'Patch_{curr_patch_version}'

                # create folder
                if not os.path.exists(f'{base_path}/{patch_folder}'):
                    os.makedirs(f'{base_path}/{patch_folder}')

                patch_base_url = f'{base_url}/{url_dir}/{patch_folder}'
                for file_name in load_files:
                    file_name = file_name.replace('#ver#', str(curr_patch_version))
                    file_url = f'{patch_base_url}/{file_name}'
                    file_path = f'{base_path}/{patch_folder}/{file_name}'

                    await download_file(file_url, file_path)

                progress_bar(total_patches - (patch_version - curr_patch_version), total_patches)

    else:
        print('Download ver data failed')


if __name__ == '__main__':
    asyncio.run(main())