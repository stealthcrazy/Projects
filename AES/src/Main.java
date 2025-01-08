import java.io.*;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		/*
		int[] array = SubByte.affineTransform(SubByte.gf_invert(43));
		System.out.println(Arrays.toString(array));
		
		System.out.println();
		System.out.println();
		System.out.println();
		System.out.println("-----------------");
		int[] array2 = SubByte.affineTransform(SubByte.gf_invert(56));
		System.out.println(Arrays.toString(array2));
		
		
		//System.out.println(SubByte.gf_invert(52));
		//System.out.println(SubByte.gf_invert(56));
		
		
		
		
		ArrayList<Integer> k = new ArrayList<Integer>();
		k.add(0xdb);
		k.add(0x0b);
		k.add(0xad);
		k.add(0x00);
		
		ArrayList<Integer> K = KeyExpansion.transformVector(k, 4);
		
		for(int i = 0 ; i<4 ; ++i) {
			System.out.println(Integer.toHexString(K.get(i)));
		}*/
		
		/*
		
		
		
		
		
		
		
		
		System.out.println(Key);
		
		System.out.println(plainText);
		
		State newState = new State(Opperations.xorArray(Key, plainText));
		System.out.println(newState);
		
	    newState.stateArray2D = Opperations.SubIntegers(newState);
	    System.out.println(newState);
	    
	    State S = new State(ShiftRows.ShiftRow(newState));
	    System.out.println(S);
	    
	    
	    
	    
	    
	    State k = new State(MixColumns.MixColumn(S));
	    System.out.println(k);
		*/
		
		//int[] T = {0,0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,0xaa,0xbb,0xcc,0xdd,0xee,0xf8};
	
		//int[] T = {0x48,0x48,0x48,0x48,0x48,0x48,0x48,0x48,0x48,0x48,0x48,0x48,0x48,0x48,0x48,0x48};
		//int[] k = {0,1,2,3,4,5,6,7,8,9,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f};
		
		//State K = new State("helloHowAreYou??");
		
		//System.out.println(K);
		
		//Cipher.Encrypt(K,"/Users/sohanprabhu/Desktop/Java Project/AES/src/test.txt");
		//ipher.Decrypt(K,"/Users/sohanprabhu/Desktop/Java Project/AES/src/test.txt");Cipher.Decrypt(K,"/Users/sohanprabhu/Desktop/Java Project/AES/src/test.txt");
		
		
		
		//InvSubByte  n = new InvSubByte(0xca);
		//System.out.println(n.InversedByte);
		
		/*s
		State Text = new State("abcdefghijklmnop");
		System.out.println(Text);
		ArrayList<ArrayList<Integer>> J = Cipher.encrypt(K,Text);
		State NJ = new State(J);
		System.out.println(NJ);
		for(int i  = 0; i<4;i++) {
			for(int j  = 0; j<4;j++) {
				System.out.print(Integer.toHexString(NJ.stateArray2D.get(j).get(i)));
			}
			
		}
		ArrayList<ArrayList<Integer>> D = Cipher.decrypt(K,NJ);
		System.out.println();
		State NJD = new State(D);
		System.out.println(NJD);
		for(int i  = 0; i<4;i++) {
			for(int j  = 0; j<4;j++) {
				System.out.print(Integer.toHexString(NJD.stateArray2D.get(j).get(i)));
			}
			
		}*/
		
		
		
		
		//fileReader f = new fileReader("/Users/sohanprabhu/Desktop/Java Project/AES/src/notes");
		
		
		/* 
		File file = new File("/Users/sohanprabhu/Desktop/Java Project/AES/src/notes");
		BufferedReader br = new BufferedReader(new FileReader(file));
		String st;
		String Bt = "";
	
		;
        // Condition holds true till
        // there is character in a string
        while ((st = br.readLine()) != null) {
 
            // Print the string
            System.out.println(st);
        	Bt+=st;
        }
        System.out.println(Bt);*/
        int[] k = {0x00,0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,0xaa,0xbb,0xcc,0xdd,0xee,0xff};
		State K = new State(k);
		State Pt = new State(k);
		Cipher.Encrypt(K,"AES/src/test.txt");
		//Cipher.Decrypt(K,"/Users/sohanprabhu/Desktop/TETRIS/word.txt");
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

	}
	
	
	
	

}
