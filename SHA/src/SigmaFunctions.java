import java.util.ArrayList;

public class SigmaFunctions {
	
	static ArrayList<Long> duplicateArray(ArrayList<Long> a1) {
		ArrayList<Long> a2 = new ArrayList<Long>();
		for(int i = 0 ; i<a1.size();i++) {
			a2.add(a1.get(i));
		}
		return a2;
		
		
	}
	
	
	static ArrayList<Long> ChF(ArrayList<Long> a1 ,ArrayList<Long> a2,ArrayList<Long> a3 ){    // Choose function Ch(x,y,z) = (x ^ y) + (~x ^ z)
		ArrayList<Long> a4 = bitXor(bitAnd(a1,a2) , bitAnd( bitComplement(a1) ,a3) );
		return a4;
	}
	static ArrayList<Long> MajF(ArrayList<Long> a1 ,ArrayList<Long> a2,ArrayList<Long> a3){   // Majority function Maj(x,y,z) = (x ^ y) + (x ^ z) + (y ^ z)
		ArrayList<Long> a4 = bitXor(bitXor(bitAnd(a1,a2) , bitAnd(a1,a3)) , bitAnd(a2,a3)) ;
		return a4;
	}
	
	static ArrayList<Long> SigmaU1(ArrayList<Long> array){  // Sigma function ∑ 
		ArrayList<Long> a1 = duplicateArray(array);
		RotateCircularRight(2,a1);
		
		ArrayList<Long> a2 = duplicateArray(array);
		RotateCircularRight(13,a2);
		ArrayList<Long> a3 = duplicateArray(array);
		RotateCircularRight(22,a3);
		
		ArrayList<Long> resultArray =  bitXor(bitXor(a1,a2) , a3);
		
		return resultArray;
	}
	static ArrayList<Long> SigmaU2(ArrayList<Long> array){
		ArrayList<Long> a1 = duplicateArray(array);
		RotateCircularRight(6,a1);
		
		ArrayList<Long> a2 = duplicateArray(array);
		RotateCircularRight(11,a2);
		ArrayList<Long> a3 = duplicateArray(array);
		RotateCircularRight(25,a3);
		
		ArrayList<Long> resultArray =  bitXor(bitXor(a1,a2) , a3);
		
		return resultArray;
	}
	static ArrayList<Long> SigmaL1(ArrayList<Long> array){
		
		ArrayList<Long> a1 = duplicateArray(array);
		RotateCircularRight(7,a1);
		
		//System.out.println(a1);
		ArrayList<Long> a2 = duplicateArray(array);
		RotateCircularRight(18,a2);
		//System.out.println(a2);
		ArrayList<Long> a3 = duplicateArray(array);
		ShiftRight(3,a3);
		//System.out.println(a3);
		ArrayList<Long>  a = bitXor(a1,a2) ;
		ArrayList<Long> resultArray =  bitXor(a, a3);
		//System.out.println(resultArray);
		
		return resultArray;
		
	}
	static ArrayList<Long> SigmaL2(ArrayList<Long> array){
		ArrayList<Long> a1 = duplicateArray(array);
		RotateCircularRight(17,a1);
		
		ArrayList<Long> a2 = duplicateArray(array);
		RotateCircularRight(19,a2);
		ArrayList<Long> a3 = duplicateArray(array);
		ShiftRight(10,a3);
		
		ArrayList<Long> resultArray =  bitXor((bitXor(a1,a2)) , a3);
		
		return resultArray;
		
	}
	
	
	
	
	
	
	static void RotateCircularRight(int n ,ArrayList<Long> array) { // keep ensures that original array isnt changed
		
		if (n!= 0){
			n-=1;
			int len = array.size();
			long[] a1 = new long[len];
			long[] a2 = new long[len];
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
	
	/*if (keep == true) {
				ArrayList<Long> temp = new ArrayList<Long>();
				
				
				for (int i =0 ; i<len;i++) {
					temp.add(a2[i]);
				}
				RotateCircularRight(n,temp,keep);
				
			}*/
	static void ShiftRight(int n ,ArrayList<Long> array) {
		
		if (n!= 0){
			n-=1;
			int len = array.size();
			long[] a1 = new long[len];
			long[] a2 = new long[len];
			for (int i =0 ; i<len;i++) {
				a1[i] = array.get(i);
			}
			
			for (int j =0 ; j<len;j++) {
				if (j!= len-1) {
					
					a2[j+1] = a1[j];
				}
				if (j== len-1) {
					
					a2[0] = 0;
					
				}
			}
			array.clear();
			for (int i =0 ; i<len;i++) {
				array.add(a2[i]);
			}
			ShiftRight(n,array);
			
			
		

			
		}
		
		
		
	}
	static ArrayList<Long> add(ArrayList<Long> array,ArrayList<Long> array2){
		long l1 = convBitArray(array);
		long l2 = convBitArray(array2);
		
		long l3 = l1+l2;
		
		
		return Mod32(l3);
	}
		
	
	static ArrayList<Long> bitXor(ArrayList<Long> array,ArrayList<Long> array2) {
		long l1 = convBitArray(array);
		long l2 = convBitArray(array2);
		
		long l3 = l1^l2;
		return getbitArray(l3);
		
	}
	
	static ArrayList<Long> bitAnd(ArrayList<Long> array,ArrayList<Long> array2) {
		long l1 = convBitArray(array);
		long l2 = convBitArray(array2);
		
		long l3 = l1&l2;
		return getbitArray(l3);
		
	}
	static ArrayList<Long> bitComplement(ArrayList<Long> array) {
		long l1 = convBitArray(array);
		
		
		long l3 = ~l1;
		return getbitArray(l3);
		
	}
	static ArrayList<Long> Mod32(long l1) {
		
		
		
		long l3 = l1 & (0xFFFFFFFFL);
		return getbitArray(l3);
		
	}
	static ArrayList<Long>  getbitArray(long x) {
		ArrayList<Long> a1 = new ArrayList<Long>();
		int k = 0;
		int pad = 0;
		String s = null;

		if (Long.toBinaryString(x).length() !=64) {
			pad = 32-Long.toBinaryString(x).length();
			//System.out.println(pad);
			s = "0".repeat(pad) +Long.toBinaryString(x);
		}
		if (Long.toBinaryString(x).length() ==64) {
			pad = 0 ;
			s = ("0".repeat(pad) +Long.toBinaryString(x)).substring(32);
		}
		
		
		
		//System.out.println(s);
		char[] c = s.toCharArray();
		
		//System.out.println(pad);
		
	
		
		
		
		for(char t : c ) {
			//System.out.println(t);
			a1.add((long) (t == '1' ? 1 : 0)); 
			
			
		}
		return a1;
		
		
		
	}
	static long convBitArray(ArrayList<Long> array) {
		String s = "";
		for (long i : array) {
			s += (i == 1 ? "1" : "0");
		}
		
		return Long.parseLong(s, 2);
		
	}
	

}
