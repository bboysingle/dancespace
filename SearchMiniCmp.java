/*
from http://www.geeksforgeeks.org/search-element-unsorted-array-using-minimum-number-comparisons/
Search an element in an unsorted array using minimum number of comparisons
Given an array of n distinct integers and an element x. 
Search the element x in the array using minimum number of comparisons.
 Any sort of comparison will contribute 1 to the count of comparisons. 
 For example, the condition used to terminate a loop, 
 will also contribute 1 to the count of comparisons each time it gets executed. 
 Expressions like while (n) {n¨C;} 
 also contribute to the count of comparisons as value of n 
 is being compared internally so as to decide whether or not to terminate the loop
 */
public class SearchMiniCmp {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	int arr[]={4, 6, 1, 5, 8};
	int n = arr.length;
	int x = 1;
	String str = search(arr, n, x);
	System.out.println(str);
	}
	public static String search(int[] arr, int n, int x)
	{
		if (arr[n-1] == x)
		{
			 return "Found";
		}
	    int backup = arr[n-1];
	    arr[n-1] = x;
	 
	    // no termination condition and thus
	    // no comparison
	    for (int i = 0; ;i++)
	    {
	        // this would be executed at-most n times
	        // and therefore at-most n comparisons
	        if (arr[i] == x)
	        {
	            // replace arr[n-1] with its actual element
	            // as in original 'arr[]'
	            arr[n-1] = backup;
	 
	            // if 'x' is found before the '(n-1)th'
	            // index, then it is present in the array
	            // final comparison
	            if (i < n-1)
	                return "Found";
	 
	            // else not present in the array
	            return "Not Found";
	        }
	    }
	}

}
