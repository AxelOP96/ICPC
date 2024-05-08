polyhedrons = int(input());
faces = 0;
for x in range(polyhedrons):
    collection = input();
    if collection == "Icosahedron":
        faces = faces +20;
    elif collection == "Tetrahedron":
        faces = faces+4;
    elif collection == "Cube":
        faces = faces+6;
    elif collection == "Octahedron":
        faces = faces+8;
    else:
        faces = faces +12;

print(faces);
