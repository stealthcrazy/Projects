import java.util.ArrayList;

public class State {
	//long reversed = ((i & 0xFFL) << 56) | ((i & 0xFF00L) << 40) | ((i & 0xFF0000L) << 24) | ((i & 0xFF000000L) << 8) | ((i & 0xFF00000000L) >>> 8) | ((i & 0xFF0000000000L) >>> 24) | ((i & 0xFF000000000000L) >>> 40) | ((i & 0xFF00000000000000L) >>> 56);
	long[][] StateArray;
	
	
	State(){
		
		this.StateArray = new long[5][5];
		TestPop();
		
		

	}
	State(String S){
		
		this.StateArray = new long[5][5];
		int k =0;
		for(int m = 0 ;m <5 ; m++) {
			for(int j = 0 ;j <5 ; j++) {
				long i = toLongFromBinString(S.substring(k,k+64));
				k+=64;
				long reversed = ((i & 0xFFL) << 56) | ((i & 0xFF00L) << 40) | ((i & 0xFF0000L) << 24) | ((i & 0xFF000000L) << 8) | ((i & 0xFF00000000L) >>> 8) | ((i & 0xFF0000000000L) >>> 24) | ((i & 0xFF000000000000L) >>> 40) | ((i & 0xFF00000000000000L) >>> 56);
				this.StateArray[m][j] = reversed;
			}
			
		}
		//TestPop();
		
		

	}
	
	static State XorStates(State A ,State B) {
		for(int i = 0 ;i <5 ; i++) {
			for(int j = 0 ;j <5 ; j++) {
				A.StateArray[i][j] ^= B.StateArray[i][j] ;
			}
			
		}
		return A;
	}
	
	
	long toLongFromBinString(String t) {
		
		long m = 0;
		if(t.substring(0,1).equals("1")) {
	        m = -1 * (Long.MAX_VALUE - Long.parseLong(t.substring(1), 2) + 1);
	    } else {
	       m =  Long.parseLong(t, 2);
	    }
		//System.out.println(Long.toHexString(m));
		return m;
	}
	
	void TestPop() {
		for(int i = 0 ;i <5 ; i++) {
			for(int j = 0 ;j <5 ; j++) {
				this.StateArray[i][j] = 0x000000000000000000L;
			}
			
		}
	}
	void displayState() {
		for(int i = 0 ;i <5 ; i++) {
			for(int j = 0 ;j <5 ; j++) {
				
				displayLane(j,i);
				
				
			}
			
		}
	}
	String displayStateString() {
		String state="";
		for(int i = 0 ;i <5 ; i++) {
			for(int j = 0 ;j <5 ; j++) {
				
				state += displayLaneS(j,i);
				
				
			}
			
		}
		return state;
	}
	
	void displayLane(int x , int y) {
		long i = this.StateArray[y][x];
		long k = ((i & 0xFFL) << 56) | ((i & 0xFF00L) << 40) | ((i & 0xFF0000L) << 24) | ((i & 0xFF000000L) << 8) | ((i & 0xFF00000000L) >>> 8) | ((i & 0xFF0000000000L) >>> 24) | ((i & 0xFF000000000000L) >>> 40) | ((i & 0xFF00000000000000L) >>> 56);
		int pad = 0;
		String s = null;
		/*
		 * 
		 binary
		if (Long.toBinaryString(k).length() !=64) {
			pad = 64-Long.toBinaryString(k).length();
			//System.out.println(pad);
			s = "0".repeat(pad) +Long.toBinaryString(k);
		}
		if (Long.toBinaryString(k).length() ==64) {
			pad = 0 ;
			s = ("0".repeat(pad) +Long.toBinaryString(k)).substring(64);
		}*/
		
		// hex 
		
		if (Long.toHexString(k).length() !=16) {
			pad = 16-Long.toHexString(k).length();
			//System.out.println(pad);
			s = "0".repeat(pad) +Long.toHexString(k).toUpperCase();
		}
		if (Long.toHexString(k).length() ==16) {
			pad = 0 ;
			s = (Long.toHexString(k)).toUpperCase();
		}
		System.out.println(s);
		
	}
	String displayLaneS(int x , int y) {
		long i = this.StateArray[y][x];
		long k = ((i & 0xFFL) << 56) | ((i & 0xFF00L) << 40) | ((i & 0xFF0000L) << 24) | ((i & 0xFF000000L) << 8) | ((i & 0xFF00000000L) >>> 8) | ((i & 0xFF0000000000L) >>> 24) | ((i & 0xFF000000000000L) >>> 40) | ((i & 0xFF00000000000000L) >>> 56);
		int pad = 0;
		String s = null;
		/*
		 * 
		 binary
		if (Long.toBinaryString(k).length() !=64) {
			pad = 64-Long.toBinaryString(k).length();
			//System.out.println(pad);
			s = "0".repeat(pad) +Long.toBinaryString(k);
		}
		if (Long.toBinaryString(k).length() ==64) {
			pad = 0 ;
			s = ("0".repeat(pad) +Long.toBinaryString(k)).substring(64);
		}*/
		
		// hex 
		
		if (Long.toHexString(k).length() !=16) {
			pad = 16-Long.toHexString(k).length();
			//System.out.println(pad);
			s = "0".repeat(pad) +Long.toHexString(k).toUpperCase();
		}
		if (Long.toHexString(k).length() ==16) {
			pad = 0 ;
			s = (Long.toHexString(k)).toUpperCase();
		}
		return s;
		
	}
	
	
	
	
	
	
	
	
	
	
	
	
}
