import java.util.ArrayList;

public class InvShiftRows {
	static ArrayList<Integer> duplicateArray(ArrayList<Integer> a1) {
		ArrayList<Integer> a2 = new ArrayList<Integer>();
		for(int i = 0 ; i<a1.size();i++) {
			a2.add(a1.get(i));
		}
		return a2;
		
		
	}
	static ArrayList<ArrayList<Integer>> InvShiftRow(State word) {
			
			ArrayList<ArrayList<Integer>> array = Opperations.copyArray(word);
			ArrayList<ArrayList<Integer>> arrayDuplicate = Opperations.copyArray(word);
			ArrayList<ArrayList<Integer>> arrayFinal = new ArrayList<ArrayList<Integer>>();
			
			arrayFinal.add(arrayDuplicate.get(0));
			for(int i = 1 ; i<4;i++) {
				
				ArrayList<Integer> arrayD =  duplicateArray(arrayDuplicate.get(i));
				
				RotateCircularRight(i,arrayD);
			
				arrayFinal.add(arrayD);
				
				
			}
			
			
			return arrayFinal;
	}
	
	
	
	static void RotateCircularRight(int n ,ArrayList<Integer> array) {
			
			if (n!= 0){
				n-=1;
				int len = array.size();
				int[] a1 = new int[len];
				int[] a2 = new int[len];
				for (int i =0 ; i<len;i++) {
					a1[i] = array.get(i);
				}
				
				for (int j =0 ; j<len;j++) {
					if (j!= len-1) {
						
						a2[j+1] = a1[j];
					}
					if (j== len-1) {
						
						a2[0] = a1[j];
						
					}
				}
				
				array.clear();
				
				for (int i =0 ; i<len;i++) {
					array.add(a2[i]);
				}
				
				RotateCircularRight(n,array);
				
				
				
				
				
			
	
				
			}
			
		
			
			
			
		}
}
