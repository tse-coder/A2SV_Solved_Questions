faces = {"Icosahedron": 20,
"Cube": 6,
"Tetrahedron": 4,
"Dodecahedron": 12,
"Octahedron" : 8}
t = int(input())
res  = 0
for _ in range(t):
    res += faces[input().strip()]
print(res)