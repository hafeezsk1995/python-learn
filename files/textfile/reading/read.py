from pathlib import Path

data_folder = Path("Documents/python/filestorage/reading")
file_to_open = data_folder / "readdata.txt"


file_pointer = open(file_to_open,'r')
f= file_pointer.read()
print("read ",f)