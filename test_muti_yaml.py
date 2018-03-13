#!/usr/bin/env python
# encoding: utf-8

from os import path
import yaml


def main():
  with open("fabric_1_0_explorer.yaml") as f:
    file_data = yaml.load_all(f)
    for data in file_data:
        print data
        print data['kind'], data['metadata']['name']


if __name__ == '__main__':
    main()
