J1_LIMIT=4
J2_LIMIT=3
visited={}
path=[]
def isValid(j1,j2):
	if j1>J1_LIMIT or j2>J2_LIMIT or j1<0 or j2<0:
		return False
	return True

def waterJug_dfs(j1,j2,target):
	
	visited[(j1,j2)]=1
	path.append((j1,j2))
	if j1 == target or j2==target:
		print(path)
		exit(0)

	if isValid(J1_LIMIT,j2) and (J1_LIMIT,j2) not in visited:
		waterJug_dfs(J1_LIMIT,j2,target)

	if isValid(j1,J2_LIMIT) and (j1,J2_LIMIT) not in visited:
		waterJug_dfs(j1,J2_LIMIT,target)

	if isValid(0,j2) and (0,j2) not in visited:
		waterJug_dfs(0,j2,target)

	if isValid(j1,0) and (j1,0) not in visited:
		waterJug_dfs(j1,0,target)

	if isValid(j1-min(j1, J2_LIMIT - j2),j2+min(j1, J2_LIMIT - j2)) and (j1-min(j1, J2_LIMIT - j2),j2+min(j1, J2_LIMIT - j2)) not in visited:
		waterJug_dfs(j1-min(j1, J2_LIMIT - j2),j2+min(j1, J2_LIMIT - j2),target)

	if isValid(j1+min(j2, J1_LIMIT - j1),j2-min(j2, J1_LIMIT - j1)) and (j1+min(j2, J1_LIMIT - j1),j2-min(j2, J1_LIMIT - j1)) not in visited:
		waterJug_dfs(j1+min(j2, J1_LIMIT - j1),j2-min(j2, J1_LIMIT - j1),target)

j1_initial=0
j2_initial=0
target=2
waterJug_dfs(j1_initial,j2_initial,target)