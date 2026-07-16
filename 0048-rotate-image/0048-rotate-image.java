class Solution {
    public static int[][] reverse(int matrix[][], int n){
        int arr[] = matrix[n];
        int left = 0;
        int right = arr.length-1;
        while(left<right){
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right]=temp;
            left+=1;
            right-=1;
        } 
        matrix[n] = arr;
        return matrix;
    }
    public void rotate(int[][] matrix) {
        //transpose
        for(int i=0;i<matrix.length;i++){
            for(int j=i;j<matrix[0].length;j++){
                if(i==j) continue;
                int temp = matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(int i=0;i<matrix.length;i++){
            matrix = reverse(matrix, i);
        }
    }
}