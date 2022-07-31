import argparse
import sys
import requests
import yaml

from schema import Schema, SchemaError, Optional

sl_url = "http://localhost:6892/v1"

ctx_schema = Schema({
    "contexts": {
        str: {
            "data": list,

        }
    }
}, ignore_extra_keys=True)

exec_schema = Schema({
    "execs": {
        str: {
            Optional("exec-env"): str,
            "type": str,
            "file-name": str,
            Optional("context"): str,
            Optional("env"): list,
            Optional("args"): list
        }
    }
}, ignore_extra_keys=True)

def create_exec(args):
    pass

# 
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
    
    # parser = argparse.ArgumentParser(prog='scriptlab')
    # subparsers = parser.add_subparsers(dest='action')

    # # Create actions
    # create_parser = subparsers.add_parser('run', help='Run code or a specific exec')


    # # Run commands
    # run_parser = subparsers.add_parser('run', help='Run code or a specific exec')
    # group = run_parser.add_mutually_exclusive_group()
    # group.add_argument('-f', '--file', help='File that will be executed')
    # group.add_argument('--exec', help='Exec id that will be executed')
    # run_parser.add_argument('--args', nargs='*', help='Arguments for the execution')
    # run_parser.add_argument('--env', nargs='*', help="Env variables for the execution")

    # args = parser.parse_args(sys.argv[1:])

    # if args.action == 'run':
    #     run_action(args)

    with open('./tests/test.yaml', 'r') as f:
        y = yaml.safe_load(f)
        f.close()

    print(y)
    print(ctx_schema.is_valid(y))