files = ["start-gcode.txt", "end-gcode.txt"]

for file in files:
    with open(file, "r") as f:
        contents = f.read()

    contents_by_line = contents.split("\n")
    for i in range(0, len(contents_by_line)):
        contents_by_line[i] = contents_by_line[i].split(";")[0]

    contents = "; ".join(contents_by_line)

    with open(f"3dpos_{file}", "w") as f:
        f.write(contents)
