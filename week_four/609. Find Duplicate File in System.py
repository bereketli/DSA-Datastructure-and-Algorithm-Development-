class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
       filestore = defaultdict(list)
       output =[]
       for file in paths:
           sp_file = file.split(" ")
           for i in range(len(sp_file) - 1, 0, -1):
               sp_content = sp_file[i].split("(")
               
               filestore["".join(sp_content[1][0: -1])].append( sp_file[0]+ "/" + sp_content[0] )
       for key in filestore:
           if len(filestore[key]) > 1:
               output.append(filestore[key])
       return output
