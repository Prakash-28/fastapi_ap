
import argparse

def parse_args():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Retrieve infrastructure details from FastAPI.")
    parser.add_argument("--role", type=str, help="Role to filter by")
    parser.add_argument("--description", type=str, help="Description to filter by")
    
    return parser.parse_args()
