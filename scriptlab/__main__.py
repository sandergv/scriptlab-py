import argparse
import sys
import requests

sl_url = "http://localhost:6892/v1"

def run_action(args):

    fc = args.file
    ec = args.exec
    if fc:
        print("aqui")
        content = ""
        with open(fc, 'r') as f:
            content = f.read()
            f.close()
        req = {
            "type": "python",
            "envs": [
                "TEST=ok=1"
            ],
            "args": ["test"],
            "content": content
        }
        
        res = requests.post(sl_url + "/run", json=req)
        
        print(res.json())


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(prog='scriptlab')
    subparsers = parser.add_subparsers(dest='action')

    #
    run_parser = subparsers.add_parser('run', help='Run code or a specific exec')
    group = run_parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', help='File that will be executed')
    group.add_argument('--exec', help='Exec id that will be executed')
    run_parser.add_argument('--args', nargs='*', help='Arguments for the execution')
    run_parser.add_argument('--env', nargs='*', help="Env variables for the execution")

    args = parser.parse_args(sys.argv[1:])

    if args.action == 'run':
        run_action(args)