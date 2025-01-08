
public class Hash {
	
	static void SHA3_224(String M) {
		int c =448;
		String Bits = "01";
		//String Bits = "1111";
		int d = 224;
		Sponge n = new Sponge(1600-c,M,Bits,d);
	}
	static void SHA3_256(String M) {
		int c =512;
		String Bits = "01";
		//String Bits = "1111";
		int d = 256;
		Sponge n = new Sponge(1600-c,M,Bits,d);
		
	}
	static void SHA3_384(String M) {
		int c =768;
		String Bits = "01";
		//String Bits = "1111";
		int d = 284;
		Sponge n = new Sponge(1600-c,M,Bits,d);
	}
	static void SHA3_512(String M) {
		int c =1024;
		String Bits = "01";
		//String Bits = "1111";
		int d = 512;
		Sponge n = new Sponge(1600-c,M,Bits,d);
	}
	static void SHAKE_128(String M,int d) {
		int c =256;
		
		String Bits = "1111";
		
		Sponge n = new Sponge(1600-c,M,Bits,d);
	}
	static void SHAKE_256(String M,int d) {
		int c =512;
		
		String Bits = "1111";
		
		Sponge n = new Sponge(1600-c,M,Bits,d);
	}

}
