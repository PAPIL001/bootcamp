
def copy_file(src_file, dest_file):
    with open(src_file, 'r') as src, open(dest_file, 'w') as dest:
        for line in src:
            dest.write(line)

# Example usage: Copy 'source.txt' to 'destination.txt'
copy_file('source.txt', 'destination.txt')
