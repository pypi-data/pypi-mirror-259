#!/usr/bin/env python
import argparse
import os
import sys

conf = None
args = None


def parse_args():
	global args
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-c', help='Path to directory containing config file css_bundler_conf.py.')
	argparser.add_argument('-i', help='Path to input file.')
	args = argparser.parse_args()
	if args.c and args.i:
		print('Not allowed to combine -c and -i arguments.')
		sys.exit()


def load_conf():
	global conf

	if not args.c:
		sys.path.insert(0, os.getcwd())
	else:
		dirname = os.path.dirname(args.c)
		print('dirname', dirname)
		sys.path.insert(0, dirname)
	try:
		import css_bundler_conf as conf
	except ModuleNotFoundError as e:
		print(f'Error: unable to load config: {e}')
		sys.exit()


def handle_imports(path, imported):
	r = ''
	f = open(path)
	parent_dir = os.path.dirname(path)

	for line in f.readlines():
		if line.startswith('@import '):
			mod_fname = line.split('@import ')[1].strip().replace('"','').replace("'",'').replace(';','')
			new_path = os.path.normpath(os.path.join(parent_dir, mod_fname))
			if new_path not in imported:
				r += handle_imports(new_path, imported)
				imported.append(new_path)
		else:
			r += line
	return r


def process_with_conf():
	for input_path in conf.SRC_FILES:
		imported = []
		input_path = os.path.normpath(os.path.join(conf.SRC_DIR, input_path))
		data = handle_imports(input_path, imported)
		out_file = os.path.basename(input_path)
		out_path = os.path.join(conf.OUT_DIR, out_file)
		print(f'{input_path} > {out_path}')
		out = open(out_path, 'w')
		out.write(data)
	

def process_direct():
	imported = []
	data = handle_imports(args.i, imported)
	print(data)


def run():
	parse_args()
	if args.i:
		process_direct()
	else:
		load_conf()
		process_with_conf()


if __name__ == 'main':
	run()
