file_paths = [
    '../Filter/12306.list', '../Filter/ABC.list', '../Filter/AppleMusic.list', 
    '../Filter/Bing.list', '../Filter/MeiTuan.list', '../Filter/Tencent.list', 
    '../Filter/XieCheng.list'
]

# Open the target file where you want to merge the content
with open('../Filter/direct.list', 'w', encoding='utf-8') as output_file:
    # Loop through each file path in the list
    for file_path in file_paths:
        # Open each file and read its content
        with open(file_path, 'r', encoding='utf-8') as input_file:
            # Write the content of the input file to the output file
            output_file.write(input_file.read())
            # Optionally, add a newline or other separator between file contents
            output_file.write('\n')
