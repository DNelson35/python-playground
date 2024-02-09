#   ("11", "10", True, 'Testing versions without subversion'),
#   ("11", "11", True, 'Test equal versions'),
#   ("10.4.6", "10.4", True, 'Adding a subversion should make this version "larger"'),
#   ("10.4", "10.4.8", False, 'Adding a subversion should make this version "larger"'),
#   ("10.4", "11", False, 'Subversion precedence is smaller than Version'),
#   ("10.4", "10.10", False, 'Version value is not the same as its decimal value'),
#   ("10.4.9", "10.5", False, 'Adding subversion does not make it larger than a greater version'),

def compare_versions(version1,version2):
    v1 = [int(x) for x in version1.split('.')]
    v2 = [int(x) for x in version2.split('.')]
    return v1 >= v2

print(compare_versions("10.4", "10.10"))