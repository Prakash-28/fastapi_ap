
from infra_api.cli import parse_args
from infra_api.api_client import get_infra_details

if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_args()
    
    # Call the function with arguments
    get_infra_details(role=args.role, description=args.description)
