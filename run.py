# ref: https://github.com/alexmercerind/youtube-search-python
from youtubesearchpython import VideosSearch
import dl
import argparse
import os
from pprint import pprint

def work(keywords):

    result = {}
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
                result[title] = 'SUCCESS'
            except:
                print('Download fail')
                result[title] = 'FAIL'
        else:
            print('Search {} fail'.format(key))
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('--output_dir', default='.')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise RuntimeError('Input file does not exist')

    if not os.path.exists(args.output_dir):
        raise RuntimeError('OutputDir does not exists')

    args.input = os.path.abspath(args.input)
    cwd = os.getcwd()

    # Switch to output_dir
    os.chdir(args.output_dir)

    with open(args.input, 'r') as f:
        keywords = f.read().splitlines()
        keywords = filter(lambda x: x, keywords)
        result = work(keywords)
        print('====== Summary =====')
        pprint(result)
        print('====================')
    
    os.chdir(cwd)

if __name__ == '__main__':
    main()