import argparse, sys, configparser
from datetime import datetime


def main(number, other_number, output):
    result = number * other_number
    print(f'[{datetime.utcnow().isoformat()}] The result is {result}', file=output)
    
if __name__ == '__main__':
    parser  = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='Config File', default='config.ini')
    parser.add_argument('-o', dest='output', type=argparse.FileType('a'), help='output file', default=sys.stdout)
    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 = int(config['DEFAULT']['n1'])
        args.n2 = int(config['DEFAULT']['n2'])
    main(args.n1, args.n2, args.output)