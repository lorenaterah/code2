#cat - concatenate and print files
import sys

def my_function(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            contents = f1.read() + f2.read()
            print(contents)
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Provide 2 files")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    my_function(file1, file2)

# python cat.py file1.txt file2.txt