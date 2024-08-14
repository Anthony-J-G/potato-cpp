import argparse
import sys

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process a 'type' and 'new_name' argument.")

    # Add 'type' argument with choices
    parser.add_argument(
        "type",
        choices=["project", "solution"],
        help="Specify the type of operation ('project' or 'solution')."
    )

    # Add 'new_name' argument
    parser.add_argument(
        "new_name",
        help="The new name to apply to the specified type."
    )

    # Parse the arguments
    args = parser.parse_args()

    # Print or process the arguments
    if args.type == "project":
        print(f"Renaming the project to '{args.new_name}'.")
    elif args.type == "solution":
        print(f"Renaming the solution to '{args.new_name}'.")
    else:
        print("Unknown type. This should never happen.")
        sys.exit(1)

if __name__ == "__main__":
    main()
