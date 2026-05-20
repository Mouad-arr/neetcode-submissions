class Solution:
    def simplifyPath(self, path: str) -> str:
        stackFolderNames=[]
        keyWords=['.','..','/']
        i,n=0,len(path)
        while i<n :
            if path[i] in keyWords :
                if path[i]=='.':
                    if i+2<n and path[i+1]=='.' and  path[i+2]=='/' :
                        if len(stackFolderNames)!=0:
                            del stackFolderNames[-1]
                        i+=3
                    elif i+2==n and path[i+1]=='.'  :
                        if len(stackFolderNames)!=0:
                            del stackFolderNames[-1]
                        i+=3
                    elif i+1<n and path[i+1]=='/' :
                        i+=1
                    elif i+1==n:
                        i+=1
                    else :
                        nom=""+path[i]
                        i+=1
                        while i<n and path[i]!='/':
                            nom+=path[i]
                            i+=1
                        stackFolderNames.append(nom)
                elif path[i]=='/' :
                    i+=1
                    while i<n and path[i]=='/':
                        i+=1
            else :
                name=""+path[i]
                i+=1
                while i<n and path[i]!='/' :
                    name+=path[i]
                    i+=1
                stackFolderNames.append(name)
        res="/"
        entre=False
        for name in stackFolderNames :
            res+=name
            res+="/"
            entre=True
        if not entre:
            return res
        return res[:len(res)-1]