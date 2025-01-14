import java.util.ArrayList;

public class MiscFunctions {
	
	static ArrayList<Long> bitArray(long[] array) {
		ArrayList<Long> a1 = new ArrayList<Long>();
		int k = 0;
		
		for (long i : array) {
			int pad = 8-Long.toBinaryString(i).length();
			
			String s = "0".repeat(pad) +Long.toBinaryString(i);
			//System.out.println(s);
			char[] c = s.toCharArray();
			
			//System.out.println(pad);
			
		
			
			
			
			for(char t : c ) {
				//System.out.println(t);
				a1.add((long) (t == '1' ? 1 : 0)); 
				
				
			}
			k+=1;
			
		}
		
		
		return a1;
		
	}

}