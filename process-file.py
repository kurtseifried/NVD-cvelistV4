#!/usr/bin/env python3
import os
import json
import argparse

def write_cve_to_file(cve_item, output_dir):
    cve_id = cve_item['cve']['CVE_data_meta']['ID']
    year = cve_id.split('-')[1]
    subdir = str(int(cve_id.split('-')[2]) // 1000) + 'xxx'
    output_path = os.path.join(output_dir, year, subdir)
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, cve_id + '.json')
    with open(output_file, 'w') as f:
        json.dump(cve_item['cve'], f, indent=2)
    print(f"Processed: {cve_id}")

def process_json_file(json_file, output_dir):
    with open(json_file, 'r') as f:
        data = json.load(f)
        cve_items = data['CVE_Items']
        for cve_item in cve_items:
            write_cve_to_file(cve_item, output_dir)

def main():
    parser = argparse.ArgumentParser(description='Process CVE JSON file and write each CVE to a separate file in the specified directory structure.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file containing CVE data.')
    parser.add_argument('--output_dir', '-o', type=str, default='output', help='Directory where the CVE files will be written. Default is "output".')
    args = parser.parse_args()

    process_json_file(args.json_file, args.output_dir)

if __name__ == "__main__":
    main()

    
