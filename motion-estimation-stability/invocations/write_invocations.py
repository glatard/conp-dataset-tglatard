#!/usr/bin/env python

import argparse
import os
import json


def main():
    parser = argparse.ArgumentParser(
               description="Writes invocations to process datasets with ovmc.")
    parser.add_argument("dataset_file",
                        help="Dataset file, one line per dataset.")
    args = parser.parse_args()
    with open(args.dataset_file) as f:
        datasets = f.readlines()
    count = 0
    for dataset in datasets:
        for algo in ['afni', 'spm', 'mcflirt', 'mcflirt_fudge',
                     'niak', 'niak_no_chained_init']:
            basename = os.path.splitext(dataset)[0]
            dataset_perturbated = basename + '_one_voxel.nii.gz'
            output_base_name = basename + '_' + algo
            invocation = {}
            invocation['dataset'] = dataset.strip()
            invocation['dataset_perturbated'] = dataset_perturbated
            invocation['algorithm'] = algo
            invocation['output_base_name'] = output_base_name
            with open('invocation_'+str(count)+'.json', 'w') as f:
                f.write(json.dumps(invocation, indent=4, sort_keys=True))
            count += 1

if __name__ == '__main__':
    main()
