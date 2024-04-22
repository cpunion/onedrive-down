import argparse
import sys
import subprocess
import base64


def create_onedrive_directdownload(onedrive_link):
    # from https://towardsdatascience.com/onedrive-as-data-storage-for-python-project-2ff8d2d3a0aa
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode(
        'utf-8').replace('/', '_').replace('+', '-').rstrip("=")
    resultUrl = "https://api.onedrive.com/v1.0/shares/u!" + \
        data_bytes64_String + "/root/content"
    return resultUrl


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str)
    parser.add_argument("-o", "--output", type=str, default=None, required=False,
                        help="Output file name")
    return parser.parse_args()


def main():
    args = parse_args()
    # check if the url is a onedrive link
    if "//1drv.ms/" not in args.url:
        print("Not a onedrive link", file=sys.stderr)
        exit(1)

    # download the flle by wget command
    runargs = ["wget"]
    if args.output:
        runargs.append("-O")
        runargs.append(args.output)
    else:
        runargs.append("--content-disposition")
    runargs.append(create_onedrive_directdownload(args.url))
    print(runargs)
    # call subprocess.run, output to stdout and stderr, and exit with the return code
    exit(subprocess.run(runargs, stdout=sys.stdout, stderr=sys.stderr).returncode)
