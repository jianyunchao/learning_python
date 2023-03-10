import json
import os
import argparse


def transform(args):
    with open(args.file_name, encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip()
            line_list = line.split('\t')
            file_name = line_list[0]
            res_list = json.loads(line_list[1]) if len(line_list) >= 2 else ''
            file_name = file_name.replace('gt', 'infer_img')
            file_name = file_name.replace('jpg', 'txt')
            file_path = args.result_dir
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            with open(os.path.join(file_path, file_name), 'w', encoding='utf-8') as new_file:
                for res in res_list:
                    transcription = res.get('transcription', '')
                    points = res.get('points', [])
                    if not transcription and not points:
                        continue
                    points_str = ','.join(str(x) for x in points) if isinstance(points, list) else ''
                    new_file.writelines(points_str + ',' + transcription + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='transform pipeline_results.txt to original format')
    parser.add_argument('--file_name', type=str, default='./pipeline_results.txt',
                        help='The path of the file to be transformed')
    parser.add_argument('--result_dir', type=str, default='./result',
                        help='Folder where transform results are stored')

    transform(parser.parse_args())
