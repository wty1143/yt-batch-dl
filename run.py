# ref: https://github.com/alexmercerind/youtube-search-python
from youtubesearchpython import VideosSearch
import dl
import argparse
import os

def work(keywords):

    for key in keywords:
        try:
            videosSearch = VideosSearch(key).result()['result'][0]
            title, id = videosSearch['title'], videosSearch['id']
        except:
            continue
        
        if title:
            print(key, title, id)
            try:
                dl.download(id)
            except:
                print('Download fail')
        else:
            print('Search {} fail'.format(key))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('--output_dir', default='.')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise RuntimeError('Input file does not exist')

    if not os.path.exists(args.output_dir):
        raise RuntimeError('OutputDir does not exists')

    with open(args.input, 'r') as f:
        keywords = f.read().splitlines()
        keywords = filter(lambda x: x, keywords)
        work(keywords)

if __name__ == '__main__':
    main()