class Solution(object):
    def dfs(self, vis, image, scolor, color, sr,sc):
        if image[sr][sc] != scolor:
            return
        vis[sr][sc] = 1
        image[sr][sc] = color
        directions = [(-1,0),(0,1), (1,0), (0, -1)]
        for r, c in directions:
            nr = sr+r
            nc = sc+c
            if 0<=nr<len(image) and 0<=nc<len(image[0]) and not vis[nr][nc]:
                self.dfs(vis, image,scolor, color, nr, nc)
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        vis = [[0]*len(image[0]) for _ in range(len(image))]
        scolor = image[sr][sc]
        self.dfs(vis, image, scolor, color, sr, sc)
        return image

        