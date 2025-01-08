// x and y flipped

public class StepMappings {
	
	
	static long rc(long t) {
		if(t %255 == 0) {
			return 1;
		}
		int R = 0x80;
		for (int i = 0 ; i<(t%0xFF);i++) {
			int LSB = R&1;
			if(LSB == 1) {
				R^=0x1C;
			}
			R = R>>1;
			R^=LSB<<7;
			//System.out.println(Integer.toBinaryString(R) );
			
		}
		
		return R>>7;
		
		
           
	}
		
	
	
	
	static  long ROTR(long x, int n) {
		
		return (x << n) | ( x >>> (64-n));
		
	}
	
	
	static long[][] Theta(State S) {
	    long[][] A = S.StateArray;
	    long[][] A1 = new long[5][5];
	    long[] C = new long[5];

	    // Calculate C
	    for (int i = 0; i < 5; i++) {
	        C[i] = A[0][i] ^ A[1][i] ^ A[2][i] ^ A[3][i] ^ A[4][i];
	    }

	    // Calculate D
	    long[] D = new long[5];
	    for (int i = 0; i < 5; i++) {
	        D[i] = C[(i + 4) % 5] ^ ROTR(C[(i + 1) % 5],1); 
	    }

	    // Calculate A1
	    for (int i = 0; i < 5; i++) {
	        for (int j = 0; j < 5; j++) {
	            A1[i][j] = A[i][j] ^ D[j];
	        }
	    }

	    return A1;
	}

	static long[][]  Rho(State S) {
		
		
		        
		int w = 64;
		
		long[][] A1 = new long[5][5];
		long[][] A = S.StateArray;
	
		int[][] offsetTable = { {0,1,190,28,91},
								{36,300,6,55,276},
								{3,10,171,153,231},
								{105,45,15,21,136},
								{210,66,253,120,78},};
		int offset=0;
				
				
		for( int i = 0 ; i<5;i++) {
			for( int j = 0 ; j<5;j++) {
				offset = offsetTable[i][j]%w;
				//System.out.println(offset);
				A1[i][j] = ROTR(A[i][j],offset);
				
			}
			
				
			
				
				
				
				
				
			
		}
		return A1;
	}
	static long[][] Pi(State S) {
		int w = 64;
		
		long[][] A1 = new long[5][5];
		long[][] A = S.StateArray;
		
		for (int i = 0; i < 5; i++) {
	        for (int j = 0; j < 5; j++) {
	            A1[i][j] = A[j][(j+(3*i))%5]	;        }
	    }
		return A1;
		
		
	}
	static long[][] Chi(State S) {
		int w = 64;
		
		long[][] A1 = new long[5][5];
		long[][] A = S.StateArray;
		
		for (int i = 0; i < 5; i++) {
	        for (int j = 0; j < 5; j++) {
	            A1[i][j] = A[i][j] ^ (~A[i][(j+1)%5] ) & A[i][(j+2)%5]	;        }
	    }
		return A1;
	}
	static long[][] Iota(State S,int Ir) {
		
		long RC = 0;
		for (int j = 0; j<7;j++) {
			RC ^= rc(j+(7*Ir)) << ((long) (Math.pow(2, j))-1);
		}
		
		//System.out.println(Long.toHexString(RC));
		long[][] A = S.StateArray;
		A[0][0] = A[0][0] ^ RC;
		return A;
	}
	
	
	
	
	
	
	
	

}
