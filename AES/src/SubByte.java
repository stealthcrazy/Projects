


public class SubByte {
	
	int[] SubedByteVector = {1, 1, 0, 0, 0, 1, 1, 0};
	int SubedByte;
	
	SubByte(int a){
		if(a == 0 ) {
			this.SubedByte = 0x63;
			
		}else {
			int Inverse = gf_invert(a);
			//System.out.println(Inverse);
			this.SubedByteVector = affineTransform(Inverse);
			//System.out.println(display());
			this.SubedByte = SByte(this.SubedByteVector);
			//System.out.println(this.SubedByte);
		}
		
		
	}
	
	public String toString() {
		return Integer.toString(this.SubedByte);
	}
	
	
	static int gf_degree(int a) {
		int res = 0;
		a>>=1;
		while(a!= 0 ) {
			a>>=1;
			res+=1;
		}
		return res;
	}
	static int gf_invert(int a) {
		int mod = 283;
		int g1 = 1;
		int g2 = 0;
		int temp = 0;
		
		
		int j = gf_degree(a) -8;
		
		while(a != 1) {
				if (j<0) {
					
					temp = mod;
					mod  = a ;
					a = temp;
					
				
					
					temp = g2;
					g2 = g1;
					g1 = temp;
				
				
					j = -j;
				}
				
				a^= mod << j;
				g1 ^= g2 << j;
				
				a%=256;
				g1%=256;
				
				j = gf_degree(a) - gf_degree(mod);
				
			
			
			
		}
	
		return g1;
		
	}
	
	
	static int[] binaryArray(int value) {
		//System.out.println(value);
		String binString = Integer.toBinaryString(value);
		for(; binString.length() < 8;) {
			binString = '0'+binString;
			
		}
		//System.out.println(binString);
		int[] binary = new int[8]; 
		for(int i = 0; i<8;++i) {
			
			binary[i] = (int) Integer.parseInt(String.valueOf(binString.charAt(i))) ; 
		}
			
		return binary;
		
		
	}
	
	
	
	
	
	static int[] xorVector(int [] array) {
		final int[] VECTOR = {1, 1, 0, 0, 0, 1, 1, 0};
		int[] newVector = new int[8];
		for(int i  = 0; i<8;++i) {
			newVector[i] = (int) (array[7-i]^VECTOR[7-i]);
		}
		return newVector;
		
	}
	
	static int[] affineTransform(int Inverse) {
		
		
		
		int[] array = binaryArray(Inverse);
		//System.out.println(display(array));
		
		final int[][] affineMatrix = {	{ 1 ,0 ,0 ,0,1 ,1 ,1 ,1 },
										{ 1, 1, 0 ,0 ,0 ,1 ,1 ,1 },
										{ 1 ,1 ,1 ,0 ,0, 0, 1, 1 },
										{ 1, 1 ,1 ,1 ,0 ,0 ,0 ,1 },
										{ 1 ,1 ,1 ,1 ,1 ,0 ,0, 0 },
										{ 0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 },
										{ 0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 },
										{ 0 ,0 ,0 ,1 ,1 ,1,1, 1 } ,};
		
		int[] resultOfMultiplicationArray = new int[8];
		int[] bitArray = new int[8];
		
		for(int i =0;i<8;++i) {
			for(int j = 0 ; j<8;++j) {
				//System.out.print(array[7-j]  + " " + affineMatrix[i][j] + "  " );
				
				
				
				bitArray[j] =(affineMatrix[i][j] & array[7-j]);
				//System.out.print(affineMatrix[i][j] & array[7-j]);
				
			}
			//System.out.println();
			//System.out.println(Arrays.toString( bitArray));
			
			resultOfMultiplicationArray[i] = Opperations.selfXorBits(bitArray);
			//System.out.println(selfXorBits(bitArray));
		}
		int[] AffinedVector = xorVector(resultOfMultiplicationArray);
		//System.out.println(display(AffinedVector));
		//System.out.println();
		//System.out.println();
		return AffinedVector   ;
		
	}
	
	
	int SByte(int[] array) {
		
		String  value = "" ;
		for(int i : array) {
			value+= Integer.toString(i);
		}
		
		
		int result = Integer.parseInt(value,2);
		//System.out.println(result);
		
		
		
		return result;
		
		
	}
	String display(){
		String array = "[ ";
		
		for(int i = 0 ; i<this.SubedByteVector.length ;++i) {
			array += this.SubedByteVector[i] + " ";
			
		}
		array+="]";
		return array;
		
		
	}
	static String display(int[] Array){
		String array = "[ ";
		
		for(int i = 0 ; i<Array.length ;++i) {
			array += Array[i] + " ";
			
		}
		array+="]";
		return array;
		
		
	}
	
	
	

	
	
	
	
	
}
